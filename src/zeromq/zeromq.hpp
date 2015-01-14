#include "czmq.h"
#include <string>
using namespace std;
#ifdef __CPLUSPLUS
extern "C"{
#endif

int router_main_c (void);
void worker_ready(const char *id, zctx_t** ctx, void** worker);
char *wait_from_router(void* worker, byte *client_id, int* client_idsize);
void send_message(void* worker, const char *message,const byte *client_id, int client_idsize, const char *smName);
void destroy_states(zctx_t **ctx, void **worker);

#ifdef __CPLUSPLUS
}
#endif

class zeromq_rpc
{
	/*
	* This class is to manage messages from and to a client. Now whenever there's a message from a client, it will receive and respond
	*
	*/ 
public:
	zeromq_rpc();
	//a static function to start router-router thread
	static void startZeroMQ();
	void register_sm(string smName);
	string wait();
	void respond(string str);
	void destroy();

public:
	zctx_t *ctx;
	void *worker;
	//the req needs to store the client_id so that it can append to the message when sending
	byte *client_id;
	int client_idsize;
	string smName;

};
