# setting up project
1. install django 4.2
2. start project called django_project
3. startapp posts
4. migrate
5. inside models **class Post(models.Model):**
6. **python manage.py makemigrations**
7. **python manage.py migrate**
8. **python manage.py createsuperuser**
9. register Post model to admin site **admin.site.register(Post)**
10. add to post mode a **__srt__():** method 
11. in root folder create templates/
12. Templates = [
13. "DIRS" : [BASE_DIR / "templates"]]
14. create home.html and add post listing using for loop  
``<ul>
{% for post in post_list %}
<li>{{ post.text }}</li>
{% endfor %}
</ul>
15. add urls file in posts 
16. create homepage view class

# setting up tests
1. inside test.py **from .models import Post**
2. **class PostTests(TestCase):**
3. anotate the setup Function **@classmethod**
4. define **def setUpTestData(cls):**
5. **cls.post = Post.objects.create(text='this is test text')**
6. then test post model content with another test function
7. install gunicorn
8. deploy