discord.py
---------------

:NOTE: This is a fork of discord.py that is kept automatically up-to-date with the **upstream/rewrite** branch of discord.py. There are slight modifications which do not change any major core compatibility. Several ``gieseladev`` repositories and others pull from here. Targeted for Python >=3.6+ using rewrite with/without voice support. 

|Python Versions| |Maintained| |License|
---------------

..  |Maintained| image:: https://img.shields.io/badge/Maintained%3F-yes-66b2b2.svg?style=flat-square&longCache=false
    :target: https://github.com/gieseladev/discord.py/graphs/commit-activity
..  |Python Versions| image:: https://img.shields.io/badge/python-3.6,_3.7,_3.8-blue.svg?style=flat-square&longCache=false
    :target: https://github.com/gieseladev/discord.py
..  |License| image:: https://img.shields.io/github/license/gieseladev/discord.py.svg?style=flat-square&longCache=false
    :target: https://github.com/gieseladev/discord.py/blob/rewrite/LICENSE

A modern, easy to use, feature-rich, and async ready API wrapper for Discord written in Python.

Key Features
-------------

- Modern Pythonic API using ``async`` and ``await``.
- Proper rate limit handling.
- 100% coverage of the supported Discord API.
- Optimised in both speed and memory.

Installing
----------

To install the development (rewrite) version, do the following:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U https://github.com/gieseladev/discord.py/archive/rewrite.zip#egg=discord.py[voice]

    # Windows
    py -3 -m pip install -U https://github.com/gieseladev/discord.py/archive/rewrite.zip#egg=discord.py[voice]

Optional Packages
~~~~~~~~~~~~~~~~~~

* PyNaCl (for voice support)

Please note that on Linux installing voice you must install the following packages via your favourite package manager (e.g. ``apt``, ``yum``, etc) before running the above commands:

* libffi-dev (or ``libffi-devel`` on some systems)
* python-dev (e.g. ``python3.6-dev`` for Python 3.6)

Quick Example
--------------

.. code:: py

    import discord

    class MyClient(discord.Client):
        async def on_ready(self):
            print('Logged on as', self.user)

        async def on_message(self, message):
            # don't respond to ourselves
            if message.author == self.user:
                return

            if message.content == 'ping':
                await message.channel.send('pong')

    client = MyClient()
    client.run('token')


Bot Example
~~~~~~~~~~~~~

.. code:: py

    import discord
    from discord.ext import commands

    bot = commands.Bot(command_prefix='>')

    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')

    bot.run('token')

You can find more examples in the examples directory.

Links
------

- `Documentation <https://discordpy.readthedocs.io/en/rewrite/>`_
- `Official Discord Server <https://discord.gg/r3sSKJJ>`_
- `Discord API <https://discord.gg/discord-api>`_
