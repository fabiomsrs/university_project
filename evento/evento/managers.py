from django.db.models.query import QuerySet

class EventoQuerySet(QuerySet):
	def eventos_satelites(self):
		return self.all().exclude(evento_principal=None)

class CupomQuerySet(QuerySet):
	def cupons_automaticos(self):
		return self.filter(isautomatico=True)

EventoSateliteManager = EventoQuerySet.as_manager
CupomAutomaticoManager = CupomQuerySet.as_manager