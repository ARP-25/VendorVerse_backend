from rest_framework import serializers
from .models import Category, Product, Gallery, Specification, Size, Color, Cart, CartOrder, CartOrderItem, ProductFaq, Review, Wishlist, Notification, Coupon, Profile
from userauths.serializer import ProfileSerializer, UserSerializer
from vendor.models import Vendor





class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = '__all__'


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'



# class ProductSerializer(serializers.ModelSerializer):
#     # Serialize related Category, Tag, and Brand models
#     # category = CategorySerializer(many=True, read_only=True)
#     # tags = TagSerializer(many=True, read_only=True)
#     gallery = GallerySerializer(many=True, read_only=True)
#     color = ColorSerializer(many=True, read_only=True)
#     size = SizeSerializer(many=True, read_only=True)
#     specification = SpecificationSerializer(many=True, read_only=True)
#     # rating = serializers.IntegerField(required=False)
    
#     # specification = SpecificationSerializer(many=True, required=False)
#     # color = ColorSerializer(many=True, required=False)
#     # size = SizeSerializer(many=True, required=False)
#     # gallery = GallerySerializer(many=True, required=False, read_only=True)

#     class Meta:
#         model = Product
#         fields = [
#             "id",
#             "title",
#             "image",
#             "description",
#             "category",
#             "tags",
#             "brand",
#             "price",
#             "old_price",
#             "shipping_amount",
#             "stock_qty",
#             "in_stock",
#             "status",
#             "type",
#             "featured",
#             "hot_deal",
#             "special_offer",
#             "digital",
#             "views",
#             "orders",
#             "saved",
#             # "rating",
#             "vendor",
#             "sku",
#             "pid",
#             "slug",
#             "date",
#             "gallery",
#             "specification",
#             "size",
#             "color",
#             "product_rating",
#             "rating_count",
#             'order_count',
#             "get_precentage",
#         ]
    
#     def __init__(self, *args, **kwargs):
#         super(ProductSerializer, self).__init__(*args, **kwargs)
#         # Customize serialization depth based on the request method.
#         request = self.context.get('request')
#         if request and request.method == 'POST':
#             # When creating a new product, set serialization depth to 0.
#             self.Meta.depth = 0
#         else:
#             # For other methods, set serialization depth to 3.
#             self.Meta.depth = 3


class ProductReadSerializer(serializers.ModelSerializer):
    gallery = GallerySerializer(many=True, read_only=True)
    color = ColorSerializer(many=True, read_only=True)
    specification = SpecificationSerializer(many=True, read_only=True)
    size = SizeSerializer(many=True, read_only=True)
    vendor = VendorSerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'image',
            'description',
            'category',
            'price',
            'old_price',
            'shipping_amount',
            'stock_qty',
            'in_stock',
            'status',
            'featured',
            'views',
            'rating',
            'vendor',
            'pid',
            'slug',
            'date',
            'gallery',
            'color',
            'specification',
            'size',
            'product_rating',
            'rating_count',
            'orders',
        ]
        depth = 3



class ProductWriteSerializer(serializers.ModelSerializer):
    specifications = SpecificationSerializer(many=True, write_only=True, required=False)
    colors = ColorSerializer(many=True, write_only=True, required=False)
    sizes = SizeSerializer(many=True, write_only=True, required=False)
    gallery = GallerySerializer(many=True, write_only=True, required=False)

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'image', 'description', 'category', 'price',
            'old_price', 'shipping_amount', 'stock_qty', 'vendor',
            'specifications', 'colors', 'sizes', 'gallery'
        ]
        depth = 3

    def create(self, validated_data):
        specifications_data = validated_data.pop('specifications', [])
        colors_data = validated_data.pop('colors', [])
        sizes_data = validated_data.pop('sizes', [])
        gallery_data = validated_data.pop('gallery', [])

        product = Product.objects.create(**validated_data)

        for spec_data in specifications_data:
            Specification.objects.create(product=product, **spec_data)
        for color_data in colors_data:
            Color.objects.create(product=product, **color_data)
        for size_data in sizes_data:
            Size.objects.create(product=product, **size_data)
        for gallery_item in gallery_data:
            Gallery.objects.create(product=product, **gallery_item)

        return product

    def update(self, instance, validated_data):
        specifications_data = validated_data.pop('specifications', [])
        colors_data = validated_data.pop('colors', [])
        sizes_data = validated_data.pop('sizes', [])
        gallery_data = validated_data.pop('gallery', [])

        instance = super().update(instance, validated_data)

        instance.specification_set.all().delete()
        instance.color_set.all().delete()
        instance.size_set.all().delete()
        instance.gallery_set.all().delete()

        for spec_data in specifications_data:
            Specification.objects.create(product=instance, **spec_data)
        for color_data in colors_data:
            Color.objects.create(product=instance, **color_data)
        for size_data in sizes_data:
            Size.objects.create(product=instance, **size_data)
        for gallery_item in gallery_data:
            Gallery.objects.create(product=instance, **gallery_item)

        return instance





class CartSerializer(serializers.ModelSerializer):
    # Serialize the related Product model
    
    product = ProductReadSerializer()  
    class Meta:
        model = Cart
        fields = '__all__'

class CartOrderItemSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer(read_only=True)
    product = ProductReadSerializer(read_only=True)
    class Meta:
        model = CartOrderItem
        fields = '__all__'


class CartOrderSerializer(serializers.ModelSerializer):
    items = CartOrderItemSerializer(many=True, read_only=True, source='cartorderitem_set')  # Adjust source according to your related name

    class Meta:
        model = CartOrder
        fields = '__all__'  # Make sure to include 'items' or adjust as necessary

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Additional logic or adjustments can be added here if needed
        return representation





class ProductFaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFaq
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductFaqSerializer, self).__init__(*args, **kwargs)
        request = kwargs.get('context', {}).get('request')
        if request.METHOD == 'POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 3





class WishlistSerializer(serializers.ModelSerializer):
    product = ProductReadSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Wishlist
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(WishlistSerializer, self).__init__(*args, **kwargs)
        request = kwargs.get('context', {}).get('request')
        if request.method.upper() == 'POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 3



class ReviewSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    product = ProductReadSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'review','reply', 'product', 'user', 'profile', 'rating', 'date']
        depth = 3





class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CouponSerializer, self).__init__(*args, **kwargs)
        request = kwargs.get('context', {}).get('request')
        if request.method.upper() == 'POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 3


class NotificationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    vendor = VendorSerializer(read_only=True)
    order = CartOrderSerializer(read_only=True)
    order_items = CartOrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Notification
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request', None)
        if request and request.method.upper() == 'POST':
            self.Meta.depth = 0
        else:
            self.Meta.depth = 3
        return representation
    

class SummarySerializer(serializers.Serializer):
    products = serializers.IntegerField()
    orders = serializers.IntegerField()
    revenue = serializers.DecimalField(max_digits=120, decimal_places=2)


class EarningSerializer(serializers.Serializer):
    monthly_revenue = serializers.DecimalField(max_digits=120, decimal_places=2)
    total_revenue = serializers.DecimalField(max_digits=120, decimal_places=2)


class CouponSummarySerializer(serializers.Serializer):
    total_coupons = serializers.IntegerField()
    active_coupons = serializers.IntegerField()

class NotificationSummarySerializer(serializers.Serializer):
    read_notification = serializers.IntegerField()
    unread_notification = serializers.IntegerField()
    all_notification = serializers.IntegerField()



    