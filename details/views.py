from django.shortcuts import render, get_object_or_404, redirect
from renderer.models import Poster, Favorite
from django.contrib.auth.decorators import login_required

# Ensure the user is logged in
@login_required
def poster_details(request, id):
    try:
        poster = Poster.objects.get(id=id)
    except Poster.DoesNotExist:
        return render(request, 'poster_details.html', {'message': 'Poster not found'})

    # Check if the logged-in user has this poster in their favorites
    is_favorite = Favorite.objects.filter(user=request.user, poster_id=poster).exists()

    # Debugging: Print the value of is_favorite
    print(f"Is favorite: {is_favorite}")

    if request.method == 'POST':
        if is_favorite:
            # Remove the poster from the user's favorites
            Favorite.objects.filter(user=request.user, poster_id=poster).delete()
            return redirect('poster_details', id=poster.id)  # Redirect to the same page
        else:
            # Add the poster to the user's favorites
            Favorite.objects.create(user=request.user, poster_id=poster)
            return redirect('poster_details', id=poster.id)  # Redirect to the same page

    return render(request, 'poster_details.html', {'poster': poster, 'is_favorite': is_favorite})
