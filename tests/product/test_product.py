from inventory_report.product import Product


def test_create_product() -> None:
    test_id = "1"
    test_product_name = "cadeira"
    test_company_name = "Target Corporation"
    test_manufacturing_date = "2021-02-18"
    test_expiration_date = "2025-09-17"
    test_serial_number = "CR25"
    test_storage_instructions = "empilhadas"

    product = Product(
        test_id,
        test_product_name,
        test_company_name,
        test_manufacturing_date,
        test_expiration_date,
        test_serial_number,
        test_storage_instructions,
    )

    assert product.id == test_id, "Erro no atributo id"
    assert (
        product.product_name == test_product_name
    ), "Erro no atributo product_name"
    assert (
        product.company_name == test_company_name
    ), "Erro no atributo company_name"
    assert (
        product.manufacturing_date == test_manufacturing_date
    ), "Erro no atributo manufacturing_date"
    assert (
        product.expiration_date == test_expiration_date
    ), "Erro no atributo expiration_date"
    assert (
        product.serial_number == test_serial_number
    ), "Erro no atributo serial_number"
    assert (
        product.storage_instructions == test_storage_instructions
    ), "Erro no atributo storage_instructions"
