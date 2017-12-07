class Organization:
    def __init__ (self, called, longName, legalName, uri, emailSuffix, dataRegistered):
       self.called = called
       self.longName = longName
       self.legalName = legalName
       self.uri = uri
       self.emailSuffix = emailSuffix
       self.dataRegistered = dataRegistered

class Company(Organization):
  def __init__(self, called, longName, legalName, uri, emailSuffix, dataRegistered):
    super().__init__(called, longName, legalName, uri, emailSuffix, dataRegistered)
    
class PortfolioCompany(Company):
  def __init__(self, called = "", longName = "", legalName = "", uri = "", emailSuffix = "", dataRegistered = ""):
    super().__init__(called, longName, legalName, uri, emailSuffix, dataRegistered)
  
makeSchool = PortfolioCompany(called = "MakeSchool", legalName = "Make Games With Us", uri = "http://makeschool.com")

print(makeSchool.legalName)