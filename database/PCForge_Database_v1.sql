

drop database if exists pcForge;
create database pcForge;
use pcForge;


-- ============================================================================================================


-- Creating Product Tables

create table CPUs ( -- also need to add image
	cpuID decimal(10) primary key, -- 10-digit ID, can be changed
    name varChar(40) not null unique, -- 40 char limit
    description text(200), -- 200 char limit
    
    coreCount decimal(2) not null, -- 00 to 99 count
    performanceGHz decimal(1, 1) not null, -- 0.0 to 9.9 GHz
    performanceBoostGHz decimal(1, 1) not null, -- 0.0 to 9.9 GHz
    microArch varChar(30) not null, -- microarchitecture, 30 char limit
    integratedGraphics varChar(30), -- 30 char limit, can be null
    priceUSD decimal(4, 2) not null, -- 0000.00 to 9999.99 dollars
    
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
	motherboardID  decimal(10) primary key, -- 10-digit ID, can be changed
    name varChar(40) not null unique, -- 40 char limit
    description text(200), -- 200 char limit
    
    -- more stuff
    priceUSD decimal(4, 2) not null, -- 0000.00 to 9999.99 dollars
    
    check (motherboardID >= 0 and priceUSD >= 0)
);

create table Memories ( -- also need to add image
	memoryID  decimal(10) primary key, -- 10-digit ID, can be changed
    name varChar(40) not null unique, -- 40 char limit
    description text(200), -- 200 char limit
    
    -- more stuff
    priceUSD decimal(4, 2) not null, -- 0000.00 to 9999.99 dollars
    
    check (memoryID >= 0 and priceUSD >= 0)
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
	graphicsID  decimal(10) primary key, -- 10-digit ID, can be changed
    name varChar(40) not null unique, -- 40 char limit
    description text(200), -- 200 char limit
    
    -- more stuff
    priceUSD decimal(4, 2) not null, -- 0000.00 to 9999.99 dollars
    
    check (graphicsID >= 0 and priceUSD >= 0)
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

-- ...


-- ============================================================================================================


-- Creating Procedures Or Functions If We Need To?

-- ...


-- ============================================================================================================


-- Creating Other Tables, Like User and Management Log-In Information

-- ...