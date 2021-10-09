from django.shortcuts import render , redirect
from django.utils import timezone
from django.contrib import messages
from django.views.decorators.http import require_POST

from .models import Coupon
from .forms import CouponApplyForm

# Create your views here.

def test(request):
    return render(request, 'dashboard.html')

def coupon_apply(request):
    now = timezone.now()
    if request.method == "POST":
        form = CouponApplyForm(data =request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                coupon = Coupon.objects.get(code__iexact=code,
                                            valid_from__lte=now,
                                            valid_to__gte=now,
                                            active=True)
                request.session['coupon.id'] = coupon.id
                return  redirect("dash")
                print('test')

            except Coupon.DoesNotExist:
                print('fichu')
                request.session['coupon.id'] = None
                messages.error(request, "le code que vous essayez n'est pas correct")


            
    else:
        form = CouponApplyForm()

    context = {'form': form}
    return render(request , 'base.html', context)