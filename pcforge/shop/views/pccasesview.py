from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product
from shop.models import PCCase

class PCCasesView(TemplateView):
    template_name = "shop/Product_Details_PCCases.html"

    def get(self, request):
        pccases = PCCase.objects.select_related("prod_id").all()
        context = {
            "pccases": [{
                "id":pccase.prod_id.id,
                "formFactor": pccase.formFactor,
                "maxGPULengthMM": pccase.maxGPULengthMM,
                "maxCPUCoolerHeightMM": pccase.maxCPUCoolerHeightMM,
                "maxPSULengthMM": pccase.maxPSULengthMM,
                "material": pccase.material,
                "sidePanelType": pccase.sidePanelType,
                "expansionSlots": pccase.expansionSlots,
                "productName": pccase.prod_id.name, 
                "productPrice": pccase.prod_id.price, 
                "productImage": pccase.prod_id.mainImage
                } for pccase in pccases]}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))