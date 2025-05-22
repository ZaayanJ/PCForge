from django.views.generic import TemplateView
from django.http import HttpResponse
from django.template import loader
from shop.models import Product
from shop.models import PCCase

class PCCasesView(TemplateView):
    template_name = "shop/Product_Details_PCCases.html"

    def get(self, request):
        pccases = PCCase.objects.select_related("prod_id").all()

                # Filter by manufacturer
        selected_manufacturer = request.GET.get('manufacturer')
        if selected_manufacturer and selected_manufacturer != "All":
            pccases = pccases.filter(prod_id__manufacturer=selected_manufacturer)

        # Filter by price
        max_price = request.GET.get('max_price')
        if max_price:
            try:
                pccases = pccases.filter(prod_id__price__lte=float(max_price))
            except ValueError:
                pass  # ignore invalid price input

        manufacturers = PCCase.objects.select_related("prod_id").values_list(
            "prod_id__manufacturer", flat=True).distinct()

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
                "productImage": pccase.prod_id.mainImage,
                "inventory": pccase.prod_id.inventory
                } for pccase in pccases],
                "manufacturers":manufacturers}
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render(context, request))