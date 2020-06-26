from api.models import db, Company, Price, Recommendation


def test_index(client):
    rs = client.get("/")
    assert rs.status_code == 200


def test_get_company_info(client):
    rs = client.get("/company-info")

    assert rs.status_code == 200
    ret_dict = rs.json
    assert ret_dict["success"] == True
    assert ret_dict["result"]["data"] == []

    # create Company and test whether it returns it
    temp_company = Company(
        address="1601 Willow Road",
        sector="Communication Services",
        short_name="Facebook, Inc.",
        ticker="FB"
    )
    db.session.add(temp_company)
    db.session.commit()

    rs = client.get("/company-info")
    ret_dict = rs.json
    assert len(ret_dict["result"]["data"]) == 1
    assert ret_dict["result"]["data"][0]["short_name"] == "Facebook"
