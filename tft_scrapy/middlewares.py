# -*- coding: utf-8 -*-

# Define aquí los modelos para tu middleware de araña
#
# Consulta la documentación en:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

class TFTChampionDataMiddleware(object):
    # No es necesario definir todos los métodos. Si un método no está definido,
    # Scrapy actúa como si el middleware de araña no modifica los objetos pasados.

    @classmethod
    def from_crawler(cls, crawler):
        # Este método es utilizado por Scrapy para crear tus arañas.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Llamado para cada respuesta que pasa por el middleware de araña
        # y entra en la araña.

        # Debería devolver None o generar una excepción.
        return None

    def process_spider_output(response, result, spider):
        # Llamado con los resultados devueltos por la araña, después
        # de que ha procesado la respuesta.

        # Debe devolver un iterable de objetos Request, dict o Item.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Llamado cuando una araña o el método process_spider_input() (de otro middleware de araña)
        # genera una excepción.

        # Debería devolver None o un iterable de objetos Response, dict o Item.
        pass

    def process_start_requests(start_requests, spider):
        # Llamado con las solicitudes iniciales de la araña, y funciona
        # de manera similar al método process_spider_output(), excepto
        # que no tiene una respuesta asociada.

        # Debe devolver solo solicitudes (no elementos).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
