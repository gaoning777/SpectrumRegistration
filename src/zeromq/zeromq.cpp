#define __CPLUSPLUS
#include "zeromq.hpp"
#include <iostream>
#include <thread>
#include <unistd.h>
#include <vector>
using namespace std;
void worker_main(string s)
{
	worker_main_c(s.c_str());
}
void router_main()
{
	router_main_c();
}
int main(void)
{	
	vector<thread> threads;
	threads.emplace_back(worker_main,"sm1");
	threads.emplace_back(worker_main,"sm2");
	thread router(router_main);
	sleep(30);
	return 0;
}
