from django.contrib import admin
from .models import Category, Post


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')#Campos de solo lectura dentro de las categorias

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('title','author','published','post_categories')#permite mostrar diferentes variables dentro de la lista del admin
    ordering = ('author','published')#Ordenarlos segun 1. autor, 2. publicación
    search_fields = ('title','content','author__username','categories__name')#Campo para realizar busquedas
    date_hierarchy = 'published' #Permite crear una submenu para desplazarse entre los posts
    list_filter = ('author__username','categories__name')#agregar los filtros que se ven a mano derecha en el admin

    def post_categories(self,obj):#Metodo para poder mostrar las categorias de los articulos en la lista
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])#Contatenando cada uno de los objetos de las categorias y serpandolas por comas, y organizandolas por nombre
    post_categories.short_description = "Categorias"#Cambiar el nombre que se ve en el admin

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)



