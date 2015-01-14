#include "czmq.h"
#define WORKER_READY   "\001"      //  Signals worker is ready

void destroy_states(zctx_t **ctx, void **worker)
{
        zsocket_destroy(*ctx,*worker);
        zctx_destroy (ctx);
}

void send_message(void* worker, const char *message,const byte *client_id, int client_idsize, const char *smName)
{
        zmsg_t *msg=zmsg_new();;
        zframe_t *wrap_frame= zframe_new(client_id,client_idsize);
        zframe_t *frame1= zframe_new(smName, strlen(smName));
        zframe_t *frame2= zframe_new(message, strlen(message));
        zmsg_append(msg,&frame1);
        zmsg_append(msg,&frame2);
        zmsg_wrap(msg, wrap_frame);
        zmsg_send(&msg, worker);
}

//the caller needs to free the message
char *wait_from_router(void* worker, byte *client_id, int *client_idsize)
{
        zmsg_t *msg=zmsg_recv(worker);
        if(!msg)
        {
                printf("interrupted when receiving messages in zeromq\n");
                return NULL;
        }
        //it will get four frames: client_id, empty frame, sm_id frame and content frame
	//zmsg_print(msg);
        zframe_t *des=zmsg_first(msg);
	*client_idsize=(int)(zframe_size(des));
        byte *tmp=zframe_data(des);
	int i=0;
	for(i=0;i<*client_idsize;i++)
	{
		*(client_id+i)=*tmp;
		tmp++;
	}
        zmsg_next(msg);
        zmsg_next(msg);
        des=zmsg_next(msg);
        return zframe_strdup(des);
}

void worker_ready(const char *id, zctx_t** ctx, void** worker)
{
        *ctx = zctx_new ();
        *worker = zsocket_new (*ctx, ZMQ_REQ);

        //  Set random identity to make tracing easier
        char identity [10];
        strncpy(identity,id,9);
        zmq_setsockopt (*worker, ZMQ_IDENTITY, identity, strlen (identity));
        zsocket_connect (*worker, "tcp://localhost:5556");

        //  Tell broker we're ready for work
        printf ("I: (%s) worker ready\n", identity);
        zframe_t *frame = zframe_new (WORKER_READY, 1);
        zframe_send (&frame, *worker, 0);
}

// router to router proxy thread
int router_main_c (void)
{
        zctx_t *ctx = zctx_new ();
        void *frontend = zsocket_new (ctx, ZMQ_ROUTER);
        void *backend = zsocket_new (ctx, ZMQ_ROUTER);
        zsocket_bind (frontend, "tcp://*:5555");    //  For clients
        zsocket_bind (backend,  "tcp://*:5556");    //  For workers

        //  Queue of available workers
        zlist_t *workers = zlist_new ();

        //  The body of this example is exactly the same as lbbroker2.
        while (true) {
                zmq_pollitem_t items [] = {
                { backend,  0, ZMQ_POLLIN, 0 },
                { frontend, 0, ZMQ_POLLIN, 0 }
                };
                //  Poll frontend only if we have available workers
                int rc = zmq_poll (items, zlist_size (workers)? 2: 1, -1);
                if (rc == -1)
                {
                        printf("interrupted during zmq_poll");
                        break;              //  Interrupted
                }
                //  Handle worker activity on backend
                if (items [0].revents & ZMQ_POLLIN) {
                        //  Use worker identity for load-balancing
                        zmsg_t *msg = zmsg_recv (backend);
                        //zmsg_print(msg);
                        if (!msg)
			{
				printf("interrupted during receive in router\n");
                                break;          //  Interrupted
			}
                        zframe_t *identity = zmsg_unwrap (msg);
                        zlist_append (workers, identity);

                        //  Forward message to client if it's not a READY
                        zframe_t *frame = zmsg_first (msg);
                        if (memcmp (zframe_data (frame), WORKER_READY, 1) == 0)
                                zmsg_destroy (&msg);
                        else
                                zmsg_send (&msg, frontend);
                }
                if (items [1].revents & ZMQ_POLLIN) {
                        //  Get client request, route to first available worker
                        zmsg_t *msg = zmsg_recv (frontend);
                        if (msg) {
                                //zmsg_wrap (msg, (zframe_t *) zlist_pop (workers));
				//zmsg_print(msg);
                                zframe_t *des=zmsg_first(msg);
                                zmsg_next(msg);
                                des=zmsg_next(msg);
				zframe_t *newdes=zframe_dup(des);
                                //zframe_t *des=zframe_new("sm1",3);
                                zmsg_wrap (msg, newdes);
                                zmsg_send (&msg, backend);
                        }
                }
        }
        //  When we're done, clean up properly
        while (zlist_size (workers)) {
                zframe_t *frame = (zframe_t *) zlist_pop (workers);
                zframe_destroy (&frame);
        }
        zlist_destroy (&workers);
        zctx_destroy (&ctx);
        return 0;
}
