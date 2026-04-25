[app]
title = NossaConsulT
package.name = nossaconsult
package.domain = org.rafaeldrones
source.dir = .
source.include_exts = py,png,jpg,json,kv,ttf
source.include_patterns = assets/*,*.png
version = 5.1

# Ajustado para 0.21.2 que apareceu no seu log de erro anterior
requirements = python3,flet==0.21.2,flet-android,requests

orientation = portrait
fullscreen = 0
android.permissions = INTERNET, WAKE_LOCK, VIBRATE
android.api = 34
android.minapi = 26
android.archs = arm64-v8a
android.uses_cleartext_traffic = True

[buildozer]
log_level = 2
warn_on_root = 1