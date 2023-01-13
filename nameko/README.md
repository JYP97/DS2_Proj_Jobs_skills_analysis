1. check the rabbitMq status and make sure it is activated
 --cmd --- : service rabbitmq-server status
2. if not activated, start it
 ---cmd--- : service rabbitmq-server start
3. go to nameko path
 ---cmd--- : cd nameko
4. run the server
 ---cmd--- : nameko run service
5. check rabbitMq Managerment
 ---web--- : http://localhost:15672/#/
 