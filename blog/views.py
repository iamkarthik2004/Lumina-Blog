from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
import random

@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            
            # Auto-assign random image similar to seed data
            images = [
                 "https://lh3.googleusercontent.com/aida-public/AB6AXuD3g_P74ear1WydbDSGURFRpW06CE-Iid_oXHRIDzFT-8FGsKEjj1Z2Xeu5i_9v-DI2okTyDUhcjzZcbT3l-CE_uWD1lGf29-RRgq0q4O1dH1IhMwtovMZ8dFqHo2L31yeFjNs8_IqNfYCtIKZBrSYgPi0eQDLRaWxzG1qFtai7zz7ceIYnR7A4poOaK-2a2IdM6xnQzPsbdZNc39QfuwnTUfIhO0NYcCDa64bSwvVQlnLFEN2OACG5uFcHrgldiDe2nsN_3wucLEY",
                 "https://lh3.googleusercontent.com/aida-public/AB6AXuCKXdczdPL1BHMhgohGpad218z6J46QIuvLkhj_2pPNy0tb9DsBLZ9XZpSZk6S5UAXWF7ikGAP2fzOakvVCFrGlZDP67fjSBdHmJCN5PFfB-UaNKksz836JD4WPaglreu2e7O56DloOvObWFAvWa_M-z4lBKszE1ZwNjCpknmUK_p2RfLO927dFKrDd99ICfB0g7mDZLHMNaWfyu6PEmRB_E4SDXd5nxNU6P0gSrPFFbgHNXcqxwNvcr3wmvZ7UAXlaUWMYWnl-bYI",
                 "https://lh3.googleusercontent.com/aida-public/AB6AXuDo0NUVcnzz-ZzcVwMy_5Beqt8k1llySYpyXEcF_1jbYPwzaAbT5NT8qJV-DIU-MvaSf9s-Ka7YoIib_wm8dAk9ZuS2B_lbTOU6FE5EtV4pqpddsKQnsR8J7AxfLVNYTEQtv1lYGhAKlrxseEHtfcrzheSfUBz5Qlo1CodnOpHYTTtl-P0oYhXi0iKuR6-f5s9yR7SbylzwUOyr7xw11iDcmWMsSTAO1bsb_QOcEu4FU1t4p4Ut_73RVZy1mDJCX1IuPL_I6i6qv0k"
            ]
            post.image_url = random.choice(images)
            post.color = random.choice(['primary', 'green-400', 'purple-400', 'pink-400']) # Random color for diversity
            
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})
