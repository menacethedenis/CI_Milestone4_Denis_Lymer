from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category, Turntable, Headphones
from django.db.models.functions import Lower
from .forms import ProductForm

# Create your views here.


def all_products(request):
    """ A view to show all products including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search terms")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | \
                Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show details about one product """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


def all_turntables(request):
    """ A view to show all turntables including sorting and search queries """

    turntables = Turntable.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                turntable = turntables.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            turntable = turntable.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            turntable = turntables.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search terms")
                return redirect(reverse('turntable'))

            queries = Q(name__icontains=query) | \
                Q(description__icontains=query)
            turntable = turntable.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'turntables': turntables,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    print(all_turntables)

    return render(request, 'products/turntables.html', context)


def turntable_detail(request, product_id):
    """ A view to show details about one turntable """

    turntable = get_object_or_404(Turntable, pk=product_id)

    context = {
        'turntable': turntable,
    }

    return render(request, 'products/turntable_detail.html', context)


@login_required
def add_turntable(request):
    """ Add a turntable to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            turntable = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[turntable.id]))
        else:
            messages.error(request, 'Failed to add product.')
    else:
        form = ProductForm()

    template = 'products/add_turntable.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_turntable(request, product_id):
    """ Edit a turntable in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    turntable = get_object_or_404(Turntable, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=turntable)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('turntable_detail', args=[turntable.id]))
        else:
            messages.error(request, 'Failed to update product.')
    else:
        form = ProductForm(instance=turntable)
        messages.info(request, f'You are editing {turntable.name}')

    template = 'products/edit_turntable.html'
    context = {
        'form': form,
        'turntable': turntable,
    }

    return render(request, template, context)


@login_required
def delete_turntable(request, product_id):
    """ Delete a turntable from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    turntable = get_object_or_404(Turntable, pk=product_id)
    turntable.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('turntables'))


def all_headphones(request):
    """ A view to show all headphones including sorting and search queries """

    headphones = Headphones.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                headphones = headphones.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            headphones = headphones.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            headphones = headphones.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search terms")
                return redirect(reverse('headphones'))

            queries = Q(name__icontains=query) | \
                Q(description__icontains=query)
            headphones = headphones.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'headphones': headphones,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/headphones.html', context)


def headphones_detail(request, product_id):
    """ A view to show details about one set of headphones """

    headphones = get_object_or_404(Headphones, pk=product_id)

    context = {
        'headphones': headphones,
    }

    return render(request, 'products/headphones_detail.html', context)


@login_required
def add_headphones(request):
    """ Add headphones to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            headphones = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[headphones.id]))
        else:
            messages.error(request, 'Failed to add product.')
    else:
        form = ProductForm()

    template = 'products/add_headphones.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_headphones(request, product_id):
    """ Edit headphones in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    headphones = get_object_or_404(Headphones, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=headphones)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('headphones_detail', args=[headphones.id]))
        else:
            messages.error(request, 'Failed to update product.')
    else:
        form = ProductForm(instance=headphones)
        messages.info(request, f'You are editing {headphones.name}')

    template = 'products/edit_headphones.html'
    context = {
        'form': form,
        'headphones': headphones,
    }

    return render(request, template, context)


@login_required
def delete_headphones(request, product_id):
    """ Delete headphones from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    headphones = get_object_or_404(Headphones, pk=product_id)
    headphones.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('headphones'))
