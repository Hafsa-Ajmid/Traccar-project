# Traccar-project
------------------------------How to use FIND ME APP----------------------------------

1-First you have to open a port in your router.

2-Then Install traccar server,Change the default port in the configuration file "default.xml" to the port you've opened.

3- Run the script"extract-data.py"(but before, make sure that you change the address of traccar in it)

4-configure Kafka Environement.

5- After that run the script "spark-Streaming.py".

6-To vizualise , you have to run the script "app.py" using Flask framework.

