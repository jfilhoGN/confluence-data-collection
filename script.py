from atlassian import Confluence
from bs4 import BeautifulSoup
import pandas as pd

if __name__ == "__main__":
  user = ""
  server = "http://xxxxxxx.com.br"
  confluence = Confluence(url=server, username=user, password="xxxxxx", cloud=True)
  page = confluence.get_page_by_id("xxxxxxxx", expand="body.storage")
  body = page["body"]["storage"]["value"]
  tables_raw = [[[cell.text for cell in row("th") + row("td")]
    for row in table("tr")]
      for table in BeautifulSoup(body, features="lxml")("table")]
  
  tables_df = [pd.DataFrame(table) for table in tables_raw]
  for table_df in tables_df:
    table_df.loc[:,2].to_csv('teste.csv', index=False)