//  Lazy Pirate client
//  Use zmq_poll to do a safe request-reply
//  To run, start lpserver and then randomly kill/restart it

#include "czmq.h"
#define REQUEST_TIMEOUT     2500    //  msecs, (> 1000!)
#define REQUEST_RETRIES     3       //  Before we abandon
#define SERVER_ENDPOINT     "tcp://localhost:5555"

int main (void)
{
    zctx_t *ctx = zctx_new ();
    printf ("I: connecting to server...\n");
    void *client = zsocket_new (ctx, ZMQ_REQ);
    assert (client);
    zsocket_connect (client, SERVER_ENDPOINT);

    int sequence = 0;
    while (!zctx_interrupted) {
        //  We send a request, then we work to get a reply
        char request [10];
        sprintf (request, "%d", ++sequence);
	zmsg_t *msg=zmsg_new();
	zframe_t* frame1=zframe_new("sm1", 3);
	zframe_t* frame2=zframe_new(request,1);
	zmsg_append(msg,&frame1);
	zmsg_append(msg,&frame2);
	zmsg_send(&msg,client);
        //zstr_send (client, request);

        int expect_reply = 1;
        while (expect_reply) {
            //  Poll socket for a reply, with timeout
            zmq_pollitem_t items [] = { { client, 0, ZMQ_POLLIN, 0 } };
            int rc = zmq_poll (items, 1, REQUEST_TIMEOUT * ZMQ_POLL_MSEC);
            if (rc == -1)
                break;          //  Interrupted

            //  .split process server reply
            //  Here we process a server reply and exit our loop if the
            //  reply is valid. If we didn't a reply we close the client
            //  socket and resend the request. We try a number of times
            //  before finally abandoning:
            
            if (items [0].revents & ZMQ_POLLIN) {
                //  We got a reply from the server, must match sequence
                zmsg_t *msg = zmsg_recv (client);
		/*
                if (atoi (reply) == sequence) {
                    printf ("I: server replied OK (%s)\n", reply);
                    expect_reply = 0;
                }
                else
                    printf ("E: malformed reply from server: %s\n",
                        reply);
		*/
		zmsg_print(msg);
		zmsg_destroy(&msg);	
		expect_reply=0;
            }
        }
	sleep(5);
    }
    zctx_destroy (&ctx);
    return 0;
}
