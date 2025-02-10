

drop database if exists pcForge;
create database pcForge;
use pcForge;


-- ============================================================================================================


-- Creating Product Tables

create table CPUs ( -- also need to add image
    cpuID decimal(10) primary key, -- 10-digit ID, can be changed
    name varChar(40) not null unique, -- 40 char limit
    description text(200), -- 200 char limit
    imageURL varChar(255) not null, -- URL to product image
    
    -- CPU specific components
    coreCount decimal(2) not null, -- 00 to 99 count
    performanceGHz decimal(1, 1) not null, -- 0.0 to 9.9 GHz
    performanceBoostGHz decimal(1, 1) not null, -- 0.0 to 9.9 GHz
    microArch varChar(30) not null, -- microarchitecture, 30 char limit
    integratedGraphics varChar(30), -- 30 char limit, can be null
    priceUSD decimal(4, 2) not null, -- 0000.00 to 9999.99 dollars
    
    -- CPU components/ingredients
    silicon varChar(50) not null,
    substrate varChar(50) not null,
    ihs varChar(50) not null, -- Integrated Heat Spreader
    
    check (cpuID >= 0 and coreCount >= 0 and performanceGHz >= 0 and performanceBoostGHz >= 0 and priceUSD >= 0)
);

create table CPUCoolers ( -- also need to add image
	cpuCoolerID decimal(10) primary key, -- 10-digit ID, can be changed
    name varChar(40) not null unique, -- 40 char limit
    description text(200), -- 200 char limit
    
    fanRPM decimal(4) not null, -- 0000 to 9999 RPM, maybe add ranged RPM? (eg. 500-1200 RPM)
    noiseLevel decimal(2, 2), -- 00.00 to 99.99 dB, can be null?
    radiatorSize decimal(3), -- 000 to 999 mm, can be null?
    priceUSD decimal(4, 2) not null, -- 0000.00 to 9999.99 dollars
    
    check (cpuCoolerID >= 0 and fanRPM >= 0 and noiseLevel >= 0 and radiatorSize >= 0 and priceUSD >= 0)
);

create table Motherboards ( -- also need to add image
    motherboardID decimal(10) primary key, -- 10-digit ID, can be changed
    name varChar(40) not null unique, -- 40 char limit
    description text(200), -- 200 char limit
    imageURL varChar(255) not null, -- URL to product image
    
    -- Motherboard specific attributes
    socketType varChar(20) not null,
    formFactor varChar(20) not null,
    chipset varChar(20) not null,
    memoryType varChar(10) not null,
    maxMemory decimal(3) not null,
    memorySlots decimal(1) not null,
    pciSlots decimal(1) not null,
    priceUSD decimal(4, 2) not null, -- 0000.00 to 9999.99 dollars
    
    -- Motherboard components/ingredients
    pcb varChar(50) not null, -- Printed Circuit Board
    vrm varChar(50) not null, -- Voltage Regulator Module
    chipsetComponent varChar(50) not null, -- Chipset Component
    
    check (motherboardID >= 0 and maxMemory > 0 and memorySlots > 0 and priceUSD >= 0)
);

create table Memories ( -- also need to add image
    memoryID decimal(10) primary key, -- 10-digit ID, can be changed
    name varChar(40) not null unique, -- 40 char limit
    description text(200), -- 200 char limit
    imageURL varChar(255) not null, -- URL to product image
    
    -- Memory specific attributes
    memoryType varChar(10) not null,
    capacity decimal(3) not null,
    speed decimal(4) not null,
    casLatency decimal(2) not null,
    modules decimal(1) not null,
    priceUSD decimal(4, 2) not null, -- 0000.00 to 9999.99 dollars
    
    -- Memory components/ingredients
    pcb varChar(50) not null, -- Printed Circuit Board
    chips varChar(50) not null, -- Memory Chips
    heatsink varChar(50) not null,
    
    check (memoryID >= 0 and capacity > 0 and speed > 0 and modules > 0 and priceUSD >= 0)
);


create table Storages ( -- also need to add image
	storageID  decimal(10) primary key, -- 10-digit ID, can be changed
    name varChar(40) not null unique, -- 40 char limit
    description text(200), -- 200 char limit
    
    -- more stuff
    priceUSD decimal(4, 2) not null, -- 0000.00 to 9999.99 dollars
    
    check (storageID >= 0 and priceUSD >= 0)
);

create table Graphics ( -- also need to add image
    graphicsID decimal(10) primary key, -- 10-digit ID, can be changed
    name varChar(40) not null unique, -- 40 char limit
    description text(200), -- 200 char limit
    imageURL varChar(255) not null, -- URL to product image
    
    -- Graphics card specific attributes
    chipset varChar(20) not null,
    memory decimal(2) not null,
    memoryType varChar(10) not null,
    coreClock decimal(4) not null,
    boostClock decimal(4),
    length decimal(3) not null,
    tdp decimal(3) not null,
    priceUSD decimal(4, 2) not null, -- 0000.00 to 9999.99 dollars
    
    -- Graphics card components/ingredients
    gpu varChar(50) not null, -- GPU Chip
    vram varChar(50) not null, -- Video Memory
    cooler varChar(50) not null, -- Cooling System
    
    check (graphicsID >= 0 and memory > 0 and coreClock > 0 and length > 0 and tdp > 0 and priceUSD >= 0)
);

create table PCCases ( -- also need to add image
	pcCaseID  decimal(10) primary key, -- 10-digit ID, can be changed
    name varChar(40) not null unique, -- 40 char limit
    description text(200), -- 200 char limit
    
    -- more stuff
    priceUSD decimal(4, 2) not null, -- 0000.00 to 9999.99 dollars
    
    check (pcCaseID >= 0 and priceUSD >= 0)
);

create table PSUs ( -- also need to add image
	psuID  decimal(10) primary key, -- 10-digit ID, can be changed
    name varChar(40) not null unique, -- 40 char limit
    description text(200), -- 200 char limit
    
    -- more stuff
    priceUSD decimal(4, 2) not null, -- 0000.00 to 9999.99 dollars
    
    check (psuID >= 0 and priceUSD >= 0)
);

-- not sure if we should do operating systems

create table Monitors ( -- also need to add image
	monitorID  decimal(10) primary key, -- 10-digit ID, can be changed
    name varChar(40) not null unique, -- 40 char limit
    description text(200), -- 200 char limit
    
    -- more stuff
    priceUSD decimal(4, 2) not null, -- 0000.00 to 9999.99 dollars
    
    check (monitorID >= 0 and priceUSD >= 0)
);

-- add more if we want, I think this is enough really


-- ============================================================================================================


-- Populating With At Least 8 Entries

-- CPUs
INSERT INTO CPUs VALUES
(1000000001, 'AMD Ryzen 7 5800X', 'High-performance 8-core processor for gaming and content creation', '/images/5800x.jpg',
8, 3.8, 4.7, 'Zen 3', NULL, 299.99,
'7nm Silicon Die', 'Organic Substrate', 'Nickel-plated Copper IHS');

INSERT INTO CPUs VALUES
(1000000002, 'Intel Core i5-12600K', '10-core hybrid architecture processor with integrated graphics', '/images/12600k.jpg',
10, 3.7, 4.9, 'Alder Lake', 'Intel UHD 770', 279.99,
'Intel 7 Process Silicon', 'Fiberglass Substrate', 'Nickel-plated Copper IHS');

-- Memory (RAM)
INSERT INTO Memories VALUES
(2000000001, 'Corsair Vengeance RGB Pro 32GB', 'High-performance RGB DDR4 RAM kit', '/images/vengeance-rgb.jpg',
'DDR4', 32, 3600, 18, 2, 129.99,
'10-layer PCB', 'Samsung B-die Chips', 'Aluminum RGB Heatsink');

INSERT INTO Memories VALUES
(2000000002, 'G.Skill Trident Z5 32GB', 'Premium DDR5 RAM kit with RGB', '/images/trident-z5.jpg',
'DDR5', 32, 6000, 36, 2, 189.99,
'8-layer PCB', 'SK Hynix Chips', 'Brushed Aluminum Heatsink');

-- Graphics Cards
INSERT INTO Graphics VALUES
(3000000001, 'NVIDIA RTX 4070 Ti', 'High-end gaming graphics card with ray tracing', '/images/4070ti.jpg',
'AD104', 12, 'GDDR6X', 2310, 2610, 305, 285, 799.99,
'NVIDIA AD104 Die', 'Micron GDDR6X', 'Triple Fan Cooling');

INSERT INTO Graphics VALUES
(3000000002, 'AMD RX 7800 XT', 'Premium 1440p and 4K gaming GPU', '/images/7800xt.jpg',
'Navi 32', 16, 'GDDR6', 2124, 2430, 276, 263, 499.99,
'TSMC 5nm Die', 'Samsung GDDR6', 'Dual Fan Cooling');

-- Motherboards
INSERT INTO Motherboards VALUES
(4000000001, 'ASUS ROG STRIX B550-F', 'Feature-rich AM4 gaming motherboard', '/images/b550f.jpg',
'AM4', 'ATX', 'B550', 'DDR4', 128, 4, 3, 199.99,
'12-layer PCB', 'DrMOS Power Stage', 'AMD B550 Chipset');

INSERT INTO Motherboards VALUES
(4000000002, 'MSI MPG Z690 EDGE', 'High-performance Intel motherboard', '/images/z690.jpg',
'LGA1700', 'ATX', 'Z690', 'DDR5', 128, 4, 4, 289.99,
'6-layer PCB', 'Titanium Power Stage', 'Intel Z690 Chipset');


-- ============================================================================================================


-- Creating Procedures Or Functions If We Need To?

-- ...


-- ============================================================================================================


-- Creating Other Tables, Like User and Management Log-In Information

-- ...