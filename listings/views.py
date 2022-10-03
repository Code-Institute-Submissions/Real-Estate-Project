from django.shortcuts import get_object_or_404, render, reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices
from django.http import HttpResponseRedirect
from .models import Listing
from .forms import CommentForm
from django.views import View


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    
    context = {
      'listings': paged_listings
    }
    
    return render(request, 'listings/listings.html', context)


class ListingDetail(View):
  
  def listing(self, request, slug, *args, **kwargs):
      queryset = Listing.objects.filter(is_published=True)
      listing = get_object_or_404(queryset, slug=slug)
      comments = listing.comments.filter(approved=True).order_by("-created_on")
      liked = False
      context = {
        'listing': listing,
        'comments': comments,
        'commented': False,
        'liked': liked,
        'comment_form': CommentForm()
        }
      if listing.likes.filter(id=self.request.user.id).exists():
        liked = True
    
      return render(request, 'listings/listing.html', context)
   

  def post(self, request, slug, *args, **kwargs):
      queryset = Listing.objects.filter(is_published=True)
      listing = get_object_or_404(queryset, slug=slug)
      comments = listing.comments.filter(approved=True).order_by("-created_on")
      liked = False
      context = {
        'listing': listing,
        'comments': comments,
        'commented': True,
        'liked': liked,
        'comment_form': comment_form
        }
      if listing.likes.filter(id=self.request.user.id).exists():
        liked = True

      comment_form = CommentForm(data=request.POST)
      if comment_form.is_valid():
        comment_form.instance.email = request.user.email
        comment_form.instance.name = request.user.username
        comment = comment_form.save(commit=False)
        comment.listing = listing
        comment.save()
      else:
        comment_form = CommentForm()

      return render(request, 'listings/listing.html', context)


class ListingLike(View):
      
  def post(self, request, slug, *args, **kwargs):
    listing = get_object_or_404(Listing, slug=slug)
    if listing.likes.filter(id=request.user.id).exists():
      listing.likes.remove(request.user)
    else:
      listing.likes.add(request.user)

    return HttpResponseRedirect(reverse('listings/listing.html', args=[slug]))
          


def search(request):
  queryset_list = Listing.objects.order_by('-list_date')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(description__icontains=keywords)

  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      queryset_list = queryset_list.filter(city__iexact=city)

  # State
  if 'state' in request.GET:
    state = request.GET['state']
    if state:
      queryset_list = queryset_list.filter(state__iexact=state)

  # Bedrooms
  if 'bedrooms' in request.GET:
    bedrooms = request.GET['bedrooms']
    if bedrooms:
      queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      queryset_list = queryset_list.filter(price__lte=price)

  context = {
    'state_choices': state_choices,
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices,
    'listings': queryset_list,
    'values': request.GET
  }

  return render(request, 'listings/search.html', context)


