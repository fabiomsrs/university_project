from django.db.models.query import QuerySet

class CupomQuerySet(QuerySet):
	def cupons_automaticos(self):
		return self.filter(isautomatico=True)

CupomAutomaticoManager = CupomQuerySet.as_manager