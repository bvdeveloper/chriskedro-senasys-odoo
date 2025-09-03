# Senasys Custom Fields Module

## Overview
This module provides custom fields and functionality for Senasys business requirements, including fixes for vendor bill unit price display and calculation issues.

## Key Features

### Vendor Bill Unit Price Fixes
- **Unit Price Display**: Fixed issue where unit price showed as $0.00 when creating vendor bills
- **Purchase Order Integration**: Unit prices from purchase orders are now properly transferred to vendor bills
- **Complete No Rounding**: Completely removed rounding from ALL subtotal calculations (create, write, onchange)
- **Example**: 70 units × $0.1871 = $13.097 (exact calculation, no rounding anywhere)

### Technical Changes

#### Account Move Line Model (`account_move_line.py`)
- Added `bill_price_unit` field for vendor bill unit price tracking
- **Completely overrode** `_get_price_total_and_subtotal_model` to prevent any currency rounding
- Added onchange methods for `price_unit`, `quantity`, and `bill_price_unit`
- **Complete removal of rounding** from all subtotal calculations:
  - `create()` method - no rounding during creation
  - `write()` method - no rounding when updating
  - `_onchange_price_subtotal()` - no rounding during onchange events
  - `_get_price_total_and_subtotal_model()` - no currency rounding
  - `_recompute_subtotal_no_rounding()` - custom method for exact calculations

#### Purchase Order Model (`purchase_order.py`)
- Updated `price_unit` field to use correct digits definition (`Unit Price`)
- Override `_prepare_account_move_line` to ensure `bill_price_unit` is set when creating vendor bills

### Calculation Method
The module now uses exact calculation without any rounding in ALL scenarios:
1. **Raw Calculation**: `raw_subtotal = price_unit × quantity`
2. **Discount Application**: Apply discount if present
3. **No Rounding Anywhere**: Use exact result without any rounding in create, write, or onchange

### Example
- **Before**: $0.1871 → rounded to $0.19 → 70 × $0.19 = $13.30
- **After**: 70 × $0.1871 = $13.097 (exact calculation, no rounding anywhere)

## Installation
1. Install the module in Odoo 15.0
2. Restart the Odoo server
3. Update the module if already installed

## Usage
- Create vendor bills as usual
- Unit prices will now display correctly and calculate without any rounding
- When creating bills from purchase orders, unit prices are automatically transferred
- Manual entry of unit prices is supported
- All existing functionality remains intact
- **No rounding occurs** during creation, editing, or onchange events

## Dependencies
- Odoo 15.0
- account module
- purchase module
- sale_management module
- product module
- stock module 