from inventory_report.product import Product


def test_product_report() -> None:
    test_product_name = "farinha"
    test_serial_number = "TY68 409C JJ43 ASD1 PL2F"
    test_manufacturing_date = "2021-05-01"
    test_company_name = "Farinini"
    test_expiration_date = "2023-06-02"
    ins = "precisa ser armazenado em local protegido da luz"

    product = Product(
        "1",
        test_product_name,
        test_company_name,
        test_manufacturing_date,
        test_expiration_date,
        test_serial_number,
        ins,
    )

    report = str(product)

    assert f"The product 1 - {test_product_name}" in report, "Erro no Trecho 1"
    assert (
        f"with serial number {test_serial_number}" in report
    ), "Erro no Trecho 2"
    assert (
        f"manufactured on {test_manufacturing_date}" in report
    ), "Erro no Trecho 3"
    assert f"by the company {test_company_name}" in report, "Erro no Trecho 4"
    assert f"valid until {test_expiration_date}" in report, "Erro no Trecho 5"
    assert (
        f"must be stored according to the following instructions: {ins}"
        in report
    ), "Erro no Trecho 6"
