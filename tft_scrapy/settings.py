# -*- coding: utf-8 -*-

# Configuración de Scrapy para el proyecto TFTChampionData
#
# Este archivo contiene configuraciones importantes y comúnmente utilizadas.
# Puedes encontrar más configuraciones en la documentación oficial:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'TFTChampionData'

# Especifica dónde se encuentran las arañas (spiders)
SPIDER_MODULES = ['TFTChampionData.spiders']
NEWSPIDER_MODULE = 'TFTChampionData.spiders'

# Configuración de las tuberías de elementos (pipelines)
ITEM_PIPELINES = {
    'TFTChampionData.pipelines.TFTChampionDataPipeline': 500,
    'TFTChampionData.pipelines.TFTChampionDataImagesPipeline': 600,
}

# Crawl de manera responsable identificando tu (y tu sitio web) en el user-agent
# USER_AGENT = 'TFTChampionData (+http://www.yourdomain.com)'

# Obedece las reglas de robots.txt
ROBOTSTXT_OBEY = True

# Directorio donde se almacenarán las imágenes descargadas
IMAGES_STORE = '/URL/DE/TU/DIRECTORIO/imagenes'
DOWNLOAD_DELAY = 2

# Configuración para el manejo de las solicitudes y la concurrencia
# CONCURRENT_REQUESTS = 32
# DOWNLOAD_DELAY = 3
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Desactiva las cookies
# COOKIES_ENABLED = False

# Configuración de las extensiones y middlewares
# SPIDER_MIDDLEWARES = {
#     'TFTChampionData.middlewares.TFTChampionDataSpiderMiddleware': 543,
# }
# DOWNLOADER_MIDDLEWARES = {
#     'TFTChampionData.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Configuración de la extensión AutoThrottle (habilitada por defecto)
# AUTOTHROTTLE_ENABLED = True
# AUTOTHROTTLE_START_DELAY = 5
# AUTOTHROTTLE_MAX_DELAY = 60
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# AUTOTHROTTLE_DEBUG = False

# Configuración de HTTP caching (desactivado por defecto)
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
