'''Setup for Feed2toot'''

from setuptools import setup, find_packages

CLASSIFIERS = [
    'Intended Audience :: End Users/Desktop',
    'Environment :: Console',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
]

setup(
    name='feed2toot',
    version='0.17',
    license='GNU GPL v3',
    description='Parse rss feeds and send new posts to Mastodon',
    long_description='Parse rss feeds and send new posts to the Mastodon social network',
    author = 'Carl Chenet',
    author_email = 'carl.chenet@ohmytux.com',
    url = 'https://gitlab.com/chaica/feed2toot',
    classifiers=CLASSIFIERS,
    download_url='https://gitlab.com/chaica/feed2toot',
    packages=find_packages(),
    scripts=['scripts/feed2toot', 'scripts/register_feed2toot_app'],
    install_requires=['beautifulsoup4', 'feedparser', 'Mastodon.py'],
    extras_require={
        'influxdb':  ["influxdb"]
    }
)
