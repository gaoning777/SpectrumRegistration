#include <iostream>
#include <thread>
#include <vector>
#include "zeromq.hpp"

void worker_main(const string id)
{
	zeromq_rpc *zmq_ins=new zeromq_rpc();
	zmq_ins->register_sm(id);
	int reply=1;
	while(reply<10)
	{
		string str=zmq_ins->wait();
		if(str=="")
		{
			printf("%s stopped\n",id.c_str());	
			return;
		}
		zmq_ins->respond(to_string(reply++));
		sleep(3);
	}
	zmq_ins->destroy();
}

int main(void)
{	
	thread router(zeromq_rpc::startZeroMQ);
	sleep(10);
	vector<thread> threads;
	threads.emplace_back(worker_main,"sm1");
	threads.emplace_back(worker_main,"sm2");
	sleep(20);
	return 0;
}
