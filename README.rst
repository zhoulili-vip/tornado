Tornado Web Server
==================

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/tornadoweb/tornado
   :target: https://gitter.im/tornadoweb/tornado?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

`Tornado <http://www.tornadoweb.org>`_ is a Python web framework and
asynchronous networking library, originally developed at `FriendFeed
<http://friendfeed.com>`_.  By using non-blocking network I/O, Tornado
can scale to tens of thousands of open connections, making it ideal for
`long polling <http://en.wikipedia.org/wiki/Push_technology#Long_Polling>`_,
`WebSockets <http://en.wikipedia.org/wiki/WebSocket>`_, and other
applications that require a long-lived connection to each user.

Hello, world
------------

将tornado应用以wsgi模式运行，可以在阿里云上使用“函数计算”功能运行成功

.. code-block:: python

    import tornado.web
	import tornado.wsgi


	class MainHandler(tornado.web.RequestHandler):
		def get(self):
			self.write("Hello, tornado")


	application = tornado.wsgi.WSGIApplication([(r"/", MainHandler)])


	def handler(environ, start_response):
		return application(environ, start_response)

This example does not use any of Tornado's asynchronous features; for
that see this `simple chat room
<https://github.com/tornadoweb/tornado/tree/stable/demos/chat>`_.

Documentation
-------------

Documentation and links to additional resources are available at
https://www.tornadoweb.org
