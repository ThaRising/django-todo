from pathlib import Path

from django.conf import settings
from django.core.management.commands import startapp

from ._utils import write_file, newlines, indent


class Command(startapp.Command):
    def handle(self, *args, **options):
        APPLICATIONS_ROOT = Path(settings.BASE_DIR) / "apps"
        APP_ROOT = APPLICATIONS_ROOT / options.get("name")

        # Create the application root
        APP_ROOT.mkdir()
        (APP_ROOT / "__init__.py").touch()
        write_file(
            APP_ROOT,
            "apps.py",
            (
                "from django.apps import AppConfig",
                *newlines(2),
                "class CoreConfig(AppConfig):",
                indent(1, f"name = '{APP_ROOT.name}'"),
            )
        )
        write_file(
            APP_ROOT,
            "urls.py",
            (
                "from django.urls import path",
                "from rest_framework import routers",
                *newlines(2),
                "router = routers.SimpleRouter()",
                newlines(),
                "urlpatterns = []",
                newlines(),
                "urlpatterns += router.urls",
            )
        )
        write_file(
            APP_ROOT,
            "admin.py",
            (
                "from django.contrib import admin",
                *newlines(2),
                "# Register your models here"
            )
        )

        # Create the migrations directory
        migrations = APP_ROOT / "migrations"
        migrations.mkdir()
        (migrations / "__init__.py").touch()

        # Create the schemas directory
        schemas = APP_ROOT / "schemas"
        schemas.mkdir()
        (schemas / "__init__.py").touch()
        write_file(
            schemas,
            "serializers.py",
            (
                "from rest_framework import serializers",
                *newlines(2),
                "# Your serializers here",
            )
        )
        write_file(
            schemas,
            "models.py",
            (
                "from django.db import models",
                *newlines(2),
                "# Your models here",
            )
        )

        # Create the templates directory
        templates = APP_ROOT / "templates"
        templates.mkdir()
        (templates / APP_ROOT.name).mkdir()
