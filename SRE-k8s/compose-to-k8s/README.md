I have constructed a fully functioning docker compose environment for monitoring and alerting
containing a simple express.js server with simple not complicated frontend built for Wdai
laboratory.
Mircoservices Stack:
- Prometheus - for monitoring, maintaining connection with web app and prometheus alermanager
- Alertmanager - for managing alerts on very low level
- Grafana - UI for monitoring and displaying graphs of data scraped by prometheus, also
can be used for managing alerts on higher level than Alertmanager with a nice UI
- Node.js - running environment for JS
- Express.js - simple JS server 
	packages working with Express.js:
	- fs
	- path
	- body-parser
	- prom-client - the most important one in terms of monitoring software
