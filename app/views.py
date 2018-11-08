from django.shortcuts     import render
from qr_code.qrcode.utils import QRCodeOptions

def index(request):
    if request.POST:
        config     = QRCodeOptions(size='M', version=1, border=6, error_correction='L')
        user_input = request.POST.get('user_input')
        return render(request, 'base.html', {'popup':True, 'config':config, 'user_input':user_input})
    return render(request, 'base.html', {})
