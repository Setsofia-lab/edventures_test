#%%
from unstructured.partition.html import partition_html

elements = partition_html(filename="")

with open("brazildata-['https:', '', 'data.worldbank.org', 'indicator', 'IT.NET.USER.ZS?locations=1W-BR'].html", "r") as f:
    elements = partition_html(file=f)

with open("/home/setsofia/dev/edventures_test/worldbankdata/brazildata-['https:', '', 'data.worldbank.org', 'indicator', 'IT.NET.USER.ZS?locations=1W-BR'].html", "r") as f:
    text = f.read()
elements = partition_html(text=text)
# %%
from llama_index.core.node_parser import HTMLNodeParser
from llama_index.core import SimpleDirectoryReader
import pickle

required_exts = [".html"]
html_reader = SimpleDirectoryReader(
    input_dir="/home/setsofia/dev/edventures_test/worldbankdata",
    required_exts=required_exts,
    recursive=True,
)
html_docs =  html_reader.load_data()
print(f"Loaded {len(html_docs)} docs")

parser = HTMLNodeParser() 

elements = parser.get_nodes_from_documents(html_docs, show_progress=True)

pickle_file = 'chunkeddata.pickle'

with open(pickle_file, 'wb') as file:
    pickle.dump(elements,file)

print(f'Chuncks elements saved to {pickle_file}')
# %%
# from unstructured_client import UnstructuredClient
# from unstructured_client.models import shared
# import pickle
# from unstructured_client.models.errors import SDKError

# s = UnstructuredClient(api_key_auth="vt1XDsTPJS6A5JMnKow12mV0autrWq")

# filename = "/home/setsofia/dev/edventures_test/worldbankdata/brazildata-['https:', '', 'data.worldbank.org', 'indicator', 'IT.NET.USER.ZS?locations=1W-BR'].html"
# file = open(filename, "rb")

# nodes = shared.PartitionParameters(
#     files=shared.Files(
#         content=file.read(),
#         file_name=filename,
#     ),
#     # Other partition params
#     strategy="auto",
#     # pdf_infer_table_structure=True,
#     # unique_element_ids=True,
# )

# chunks = s.general.partition(nodes)
# chunks.elements

# pickle_file = 'povertyheadcount.pickle'

# with open(pickle_file, 'wb') as file:
#     pickle.dump(chunks.elements,file)

# print(f'Chuncks elements saved to {pickle_file}')
# %%
