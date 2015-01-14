#define __CPLUSPLUS
#include "zeromq.hpp"
#include <iostream>
#include <thread>
#include <unistd.h>
#include <vector>
using namespace std;

zeromq_rpc::zeromq_rpc():
	ctx()
	, worker()
	, smName()
{
	client_id=new byte[20];//zeromq router will generate id less than 20 chars 
}

//called by the Server/Main.cc to run the router thread
void zeromq_rpc::startZeroMQ() 
{
	router_main_c();
}

//called by Server/Globals.cc to send a ready message to router
void zeromq_rpc::register_sm(string smName)
{
	this->smName=smName;
	worker_ready(smName.c_str(),&ctx, &worker);
}

//called by Event/Loop.c to wait for messages
string zeromq_rpc::wait()
{
	char *returnstr=wait_from_router(worker, client_id, &client_idsize);
	byte *cur=client_id;
	if(returnstr==NULL)
		return "";
	string str(returnstr);
	return str;
}

void zeromq_rpc::respond(string str)
{
	send_message(worker,str.c_str(),client_id,client_idsize,smName.c_str());
}

void zeromq_rpc::destroy()
{
	destroy_states(&ctx, &worker);
}



