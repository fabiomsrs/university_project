from django.db.models.query import QuerySet

class EventoQuerySet(QuerySet):
	def eventos_satelites(self):
		return self.all().exclude(evento_principal=None)

EventoSateliteManager = EventoQuerySet.as_manager