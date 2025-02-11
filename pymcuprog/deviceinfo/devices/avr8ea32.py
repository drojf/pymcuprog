
"""
Required device info for the avr8ea32 devices
The following data was collected from device pack Microchip.AVR-EA_DEV_DFP 1.0.28
"""

from pymcuprog.deviceinfo.eraseflags import ChiperaseEffect

DEVICE_INFO = {
    'interface': 'UPDI',
    'name': 'avr8ea32',
    'architecture': 'avr8x',

    # eeprom
    'eeprom_address_byte': 0x00001400,
    'eeprom_size_bytes': 0x0200,
    'eeprom_page_size_bytes': 0x8,
    'eeprom_read_size_bytes': 1,
    'eeprom_write_size_bytes': 1,
    'eeprom_chiperase_effect': ChiperaseEffect.CONDITIONALLY_ERASED_AVR,
    'eeprom_isolated_erase': True,

    # fuses
    'fuses_address_byte': 0x00001050,
    'fuses_size_bytes': 0x09,
    'fuses_page_size_bytes': 1,
    'fuses_read_size_bytes': 1,
    'fuses_write_size_bytes': 1,
    'fuses_chiperase_effect': ChiperaseEffect.NOT_ERASED,
    'fuses_isolated_erase': False,

    # internal_sram
    'internal_sram_address_byte': 0x7c00,
    'internal_sram_size_bytes': 0x0400,
    'internal_sram_page_size_bytes': 1,
    'internal_sram_read_size_bytes': 1,
    'internal_sram_write_size_bytes': 1,
    'internal_sram_chiperase_effect': ChiperaseEffect.NOT_ERASED,
    'internal_sram_isolated_erase': False,

    # lockbits
    'lockbits_address_byte': 0x00001040,
    'lockbits_size_bytes': 0x4,
    'lockbits_page_size_bytes': 1,
    'lockbits_read_size_bytes': 1,
    'lockbits_write_size_bytes': 1,
    'lockbits_chiperase_effect': ChiperaseEffect.ALWAYS_ERASED,
    'lockbits_isolated_erase': False,

    # signatures
    'signatures_address_byte': 0x00001100,
    'signatures_size_bytes': 0x3,
    'signatures_page_size_bytes': 0x80,
    'signatures_read_size_bytes': 1,
    'signatures_write_size_bytes': 0,
    'signatures_chiperase_effect': ChiperaseEffect.NOT_ERASED,
    'signatures_isolated_erase': False,

    # user_row
    'user_row_address_byte': 0x00001080,
    'user_row_size_bytes': 0x40,
    'user_row_page_size_bytes': 0x40,
    'user_row_read_size_bytes': 1,
    'user_row_write_size_bytes': 0x40,
    'user_row_chiperase_effect': ChiperaseEffect.NOT_ERASED,
    'user_row_isolated_erase': True,

    # flash
    'flash_address_byte': 0x00800000,
    'flash_size_bytes': 0x2000,
    'flash_page_size_bytes': 0x40,
    'flash_read_size_bytes': 2,
    'flash_write_size_bytes': 0x40,
    'flash_chiperase_effect': ChiperaseEffect.ALWAYS_ERASED,
    'flash_isolated_erase': True,

    # Some extra AVR specific fields
    'address_size': '24-bit',
    'prog_clock_khz': 1800,
    'device_id': 0x1E932B,
    'nvmctrl_base': 0x00001000,
    'syscfg_base': 0x00000F00,
    'ocd_base': 0x00000F80,

}
