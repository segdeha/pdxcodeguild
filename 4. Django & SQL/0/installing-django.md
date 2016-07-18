# Installing Django

The official Django documentation contains a good guide to installing the framework. Here, I’ve sifted through the extra information to pull out just what you need to pay attention to.

------

## Is Django already installed?

You can verify whether or not you have Django installed by going into your Python shell and typing the following:

    >>> import django

If that command throws an error, you do not have Django installed.

If you do have Django installed, you can see what version you have by running the following command (after you run the one above):

    >>> print(django.get_version())

The latest stable version is 1.9. If you have a version prior to 1.9 installed, you’ll need to uninstall that version before reinstalling.

------

## Uninstall Old Versions

If you’ve installed Django in the past, you may need to uninstall it before you install the latest version. Here are [directions for uninstalling an old version of Django](https://docs.djangoproject.com/en/1.9/topics/install/#removing-old-versions-of-django).

------

## Install Django

OK, with all of that out of the way, we’re ready to install Django. The simplest way to do this is using pip. You can test whether you have pip installed by doing the following, familiar-to-the-point-of-being-routine command:

    pip --version

If, for some reason, you don’t have pip installed, you can follow these [installation instructions](http://softwaretester.info/install-and-upgrade-pip-on-mac-os-x/).

Once you have pip installed and updated to the latest version, you can install Django using the following command:

    pip install Django
