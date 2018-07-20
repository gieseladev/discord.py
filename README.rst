discord.py
---------------

NOTE: This is a fork of discord.py that is kept automatically up-to-date with the **upstream/rewrite** branch of discord.py. There are slight modifications which do not change any major core compatibility. Several GieselaDev repos and others pull from here. Targeted for Python >=3.6+ using rewrite with voice. 

|Python Versions| |Maintained| |License|
---------------

..  |Maintained| image:: https://img.shields.io/badge/Maintained%3F-yes-66b2b2.svg?style=flat-square&longCache=false
    :target: https://github.com/GieselaDev/discord.py/graphs/commit-activity
..  |Python Versions| image:: https://img.shields.io/badge/python-3.6,_3.7-blue.svg?style=flat-square&longCache=false
    :target: https://github.com/GieselaDev/discord.py
..  |License| image:: https://img.shields.io/github/license/GieselaDev/discord.py.svg?style=flat-square&longCache=false
    :target: https://github.com/GieselaDev/discord.py/blob/rewrite/LICENSE

Info
---------------
discord.py is an API wrapper for Discord written in Python.

This was written to allow easier writing of bots or chat logs. Make sure to familiarise yourself with the API using the `documentation <https://discordpy.readthedocs.io/en/rewrite/>`__.

Breaking Changes
---------------

The discord API is constantly changing and the wrapper API is as well. There will be no effort to keep backwards compatibility in versions before ``v1.0.0``.

I recommend joining either the `official discord.py server <https://discord.gg/r3sSKJJ>`_ or the `Discord API server <https://discord.gg/discord-api>`_ for help and discussion about the library.

Installing
----------

To install the development version, do the following:

.. code:: sh

    python3 -m pip install -U https://github.com/GieselaDev/discord.py/archive/rewrite.zip#egg=discord.py[voice]

or the more long winded from cloned source:

.. code:: sh

    $ git clone https://github.com/GieselaDev/discord.py.git --branch rewrite
    $ cd discord.py
    $ python3 -m pip install -U .[voice]

Please note that on Linux installing voice you must install the following packages via your favourite package manager (e.g. ``apt``, ``yum``, etc) before running the above command:

* libffi-dev (or ``libffi-devel`` on some systems)
* python-dev (e.g. ``python3.6-dev`` for Python 3.6)

Quick Example
------------

.. code:: py

    import discord
    import asyncio

    class MyClient(discord.Client):
        async def on_ready(self):
            print('Logged in as')
            print(self.user.name)
            print(self.user.id)
            print('------')

        async def on_message(self, message):
            # don't respond to ourselves
            if message.author == self.user:
                return
            if message.content.startswith('!test'):
                counter = 0
                tmp = await message.channel.send('Calculating messages...')
                async for msg in message.channel.history(limit=100):
                    if msg.author == message.author:
                        counter += 1

                await tmp.edit(content='You have {} messages.'.format(counter))
            elif message.content.startswith('!sleep'):
                with message.channel.typing():
                    await asyncio.sleep(5.0)
                    await message.channel.send('Done sleeping.')

    client = MyClient()
    client.run('token')

You can find examples in the examples directory.

Requirements
------------

* Python 3.6.3+
* ``aiohttp`` library
* ``websockets`` library
* ``PyNaCl`` library (optional, for voice only)

  - On Linux systems this requires the ``libffi`` library. You can install in
    debian based systems by doing ``sudo apt-get install libffi-dev``.

Usually ``pip`` will handle these for you.

