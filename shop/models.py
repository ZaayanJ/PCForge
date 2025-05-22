from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
from django.utils.text import slugify


class Product(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    name = models.CharField(max_length=255)
    description = models.TextField()
    mainImage = models.CharField(max_length=255, default="missing.png")
    inventory = models.PositiveIntegerField(default=5)
    timesOrdered = models.PositiveIntegerField(default=0)
    slug = models.SlugField(max_length=255, unique=False, blank=True, null=True)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    incompatibilities = models.ManyToManyField(
        'self',
        blank=True,
        symmetrical=False,
        related_name='incompatible_with_products'
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    

    def __str__(self):
        return f"{self.name} ({self.id})"

class Image(models.Model):
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.CharField(max_length=255, default="missing.png")

class CPU(models.Model):
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    coreCount = models.PositiveIntegerField()
    baseClockSpeedGHz = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    boostClockSpeedGHz = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    microArch = models.CharField(max_length=255)
    integratedGraphics = models.CharField(max_length=255)
    integratedHeatSpreader = models.CharField(max_length=255)
    siliconType = models.CharField(max_length=255)
    substrate = models.CharField(max_length=255)
  
class Memory(models.Model):
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    memoryType = models.CharField(max_length=255)
    speedMHz = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    capacityGB = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    casLatency = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    modules = models.PositiveIntegerField()
    printedCircuitBoard = models.CharField(max_length=255)
    chips = models.CharField(max_length=255)
    heatsink = models.CharField(max_length=255)
    
class GPU(models.Model):
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    chipset = models.CharField(max_length=255)
    memoryType = models.CharField(max_length=255)
    memoryGB = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    baseClockSpeedGHz = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    boostClockSpeedGHz = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    lengthMM = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    widthMM = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    gpuChip = models.CharField(max_length=255)
    vramType = models.CharField(max_length=255)
    vramGB = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])

class Motherboard(models.Model):
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    socket = models.CharField(max_length=255)
    chipset = models.CharField(max_length=255)
    formFactor = models.CharField(max_length=255)
    maxMemoryGB = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    maxMemorySlots = models.PositiveIntegerField()
    printedCircuitBoard = models.CharField(max_length=255)
    voltageRegulator = models.CharField(max_length=255)

class CPUCooler(models.Model):
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    coolerType = models.CharField(max_length=255)  # Air, Liquid, etc.
    fanSizeMM = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    rpm = models.PositiveIntegerField()
    noiseLeveldBA = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    tdpWatts = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])  # Cooling capacity
    material = models.CharField(max_length=255)  # Aluminum, Copper, etc.
    socketCompatibility = models.CharField(max_length=255)  # Compatible CPU sockets

class Storage(models.Model):
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    storageType = models.CharField(max_length=255)  # HDD, SSD, NVMe, etc.
    capacityGB = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    readSpeedMBps = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    writeSpeedMBps = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    interface = models.CharField(max_length=255)  # SATA, PCIe, etc.
    formFactor = models.CharField(max_length=255)  # 2.5", M.2, etc.
    nandType = models.CharField(max_length=255)  # TLC, QLC, etc. (for SSDs)

class PCCase(models.Model):
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    formFactor = models.CharField(max_length=255)  # ATX, MicroATX, etc.
    maxGPULengthMM = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    maxCPUCoolerHeightMM = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    maxPSULengthMM = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    material = models.CharField(max_length=255)  # Steel, Aluminum, etc.
    sidePanelType = models.CharField(max_length=255)  # Tempered Glass, Mesh, etc.
    expansionSlots = models.PositiveIntegerField()

class PSU(models.Model):
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    wattage = models.PositiveIntegerField()  # Total power output
    efficiencyRating = models.CharField(max_length=255)  # 80 Plus Bronze, Gold, etc.
    formFactor = models.CharField(max_length=255)  # ATX, SFX, etc.
    modularity = models.CharField(max_length=255)  # Non-Modular, Semi-Modular, Fully Modular
    fanSizeMM = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    protections = models.CharField(max_length=255)  # OVP, OCP, SCP, etc.

class Monitor(models.Model):
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    screenSizeInches = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    resolution = models.CharField(max_length=255)  # 1920x1080, 2560x1440, etc.
    refreshRateHz = models.PositiveIntegerField()
    responseTimeMS = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    panelType = models.CharField(max_length=255)  # IPS, TN, VA, OLED
    aspectRatio = models.CharField(max_length=255)  # 16:9, 21:9, etc.
    ports = models.CharField(max_length=255)  # HDMI, DisplayPort, USB-C, etc.

class Customer(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    # profilePicture = models.CharField(max_length=255)
    # userType = models.CharField(max_length=255)

class Order(models.Model):
    class Status(models.TextChoices):
        PLACED = 'placed', 'Placed'
        CLAIMED = 'claimed', 'Claimed'
        PROCESSING = 'processing', 'Processing'
        SHIPPED = 'shipped', 'Shipped'
        FINISHED = 'finished', 'Finished'

    orderId = models.AutoField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="customer_order")
    employeeId = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="employee_claimed_order")
    timestamp = models.DateTimeField(auto_now_add=True)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PLACED
    )

class OrderItem(models.Model):
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    employeeId = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="employee_claimed_order_items")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="customer_order_items")
    price = models.DecimalField(max_digits=7, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])

class UserAnalytics(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    login_count = models.PositiveIntegerField(default=0)
    orders_placed = models.PositiveIntegerField(default=0)  # for regular customers
    orders_worked_on = models.PositiveIntegerField(default=0)  # for employees/admins
    orders_finished = models.PositiveIntegerField(default=0)  # for employees/admins

    def __str__(self):
        return f"Analytics for {self.user.username}"

class ContactInformation(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
    ('new', 'New'),
    ('read', 'Read'),
    ('responded', 'Responded'),
        )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')

    def __str__(self):
        return f"Message from {self.email} ({self.user})"