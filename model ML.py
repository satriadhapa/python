# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:14.116062Z","iopub.execute_input":"2022-10-31T04:33:14.116611Z","iopub.status.idle":"2022-10-31T04:33:14.129973Z","shell.execute_reply.started":"2022-10-31T04:33:14.11657Z","shell.execute_reply":"2022-10-31T04:33:14.128791Z"}}
# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

from datetime import datetime
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:14.964093Z","iopub.execute_input":"2022-10-31T04:33:14.965333Z","iopub.status.idle":"2022-10-31T04:33:17.305572Z","shell.execute_reply.started":"2022-10-31T04:33:14.965293Z","shell.execute_reply":"2022-10-31T04:33:17.30433Z"}}
customers = pd.read_csv(
    "../input/brazilian-ecommerce/olist_customers_dataset.csv")
geolocation = pd.read_csv(
    "../input/brazilian-ecommerce/olist_geolocation_dataset.csv")
items = pd.read_csv(
    "../input/brazilian-ecommerce/olist_order_items_dataset.csv")
payments = pd.read_csv(
    "../input/brazilian-ecommerce/olist_order_payments_dataset.csv")
reviews = pd.read_csv(
    "../input/brazilian-ecommerce/olist_order_reviews_dataset.csv")
orders = pd.read_csv("../input/brazilian-ecommerce/olist_orders_dataset.csv")
product = pd.read_csv(
    "../input/brazilian-ecommerce/olist_products_dataset.csv")
sellers = pd.read_csv("../input/brazilian-ecommerce/olist_sellers_dataset.csv")
products_category = pd.read_csv(
    "../input/brazilian-ecommerce/product_category_name_translation.csv")

print(customers.shape)
print(geolocation.shape)
print(items.shape)
print(payments.shape)
print(reviews.shape)
print(orders.shape)
print(product.shape)
print(sellers.shape)
print(products_category.shape)

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:17.307981Z","iopub.execute_input":"2022-10-31T04:33:17.308442Z","iopub.status.idle":"2022-10-31T04:33:17.322087Z","shell.execute_reply.started":"2022-10-31T04:33:17.308397Z","shell.execute_reply":"2022-10-31T04:33:17.320802Z"}}
customers.head()

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:17.323614Z","iopub.execute_input":"2022-10-31T04:33:17.324065Z","iopub.status.idle":"2022-10-31T04:33:17.332825Z","shell.execute_reply.started":"2022-10-31T04:33:17.324021Z","shell.execute_reply":"2022-10-31T04:33:17.331577Z"}}
customers.shape

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:17.335492Z","iopub.execute_input":"2022-10-31T04:33:17.335938Z","iopub.status.idle":"2022-10-31T04:33:17.392259Z","shell.execute_reply.started":"2022-10-31T04:33:17.335902Z","shell.execute_reply":"2022-10-31T04:33:17.391172Z"}}
customers.drop_duplicates(subset="customer_unique_id", keep="first")

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:17.393633Z","iopub.execute_input":"2022-10-31T04:33:17.393943Z","iopub.status.idle":"2022-10-31T04:33:17.555012Z","shell.execute_reply.started":"2022-10-31T04:33:17.393914Z","shell.execute_reply":"2022-10-31T04:33:17.554047Z"}}
customers2 = customers.groupby(["customer_unique_id"], as_index=False).agg({"customer_id": ["count"]
                                                                            })

customers2.columns = list(map(''.join, customers2.columns.values))

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:17.556162Z","iopub.execute_input":"2022-10-31T04:33:17.556478Z","iopub.status.idle":"2022-10-31T04:33:17.56859Z","shell.execute_reply.started":"2022-10-31T04:33:17.556448Z","shell.execute_reply":"2022-10-31T04:33:17.567561Z"}}
customers2

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:17.56993Z","iopub.execute_input":"2022-10-31T04:33:17.570285Z","iopub.status.idle":"2022-10-31T04:33:17.582738Z","shell.execute_reply.started":"2022-10-31T04:33:17.570254Z","shell.execute_reply":"2022-10-31T04:33:17.581562Z"}}
customers2["customer_idcount"].value_counts()

# %% [markdown]
# merging trx with customers

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:17.584046Z","iopub.execute_input":"2022-10-31T04:33:17.584366Z","iopub.status.idle":"2022-10-31T04:33:17.603588Z","shell.execute_reply.started":"2022-10-31T04:33:17.584317Z","shell.execute_reply":"2022-10-31T04:33:17.602312Z"}}
orders.head()

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:17.605055Z","iopub.execute_input":"2022-10-31T04:33:17.605511Z","iopub.status.idle":"2022-10-31T04:33:17.623457Z","shell.execute_reply.started":"2022-10-31T04:33:17.605469Z","shell.execute_reply":"2022-10-31T04:33:17.622223Z"}}
orders["order_status"].value_counts()

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:17.629563Z","iopub.execute_input":"2022-10-31T04:33:17.629901Z","iopub.status.idle":"2022-10-31T04:33:17.663748Z","shell.execute_reply.started":"2022-10-31T04:33:17.629871Z","shell.execute_reply":"2022-10-31T04:33:17.66259Z"}}
orders2 = orders[((orders["order_status"] != "canceled") &
                  (orders["order_status"] != "unavailable"))]

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:17.665513Z","iopub.execute_input":"2022-10-31T04:33:17.66584Z","iopub.status.idle":"2022-10-31T04:33:17.680378Z","shell.execute_reply.started":"2022-10-31T04:33:17.665809Z","shell.execute_reply":"2022-10-31T04:33:17.679207Z"}}
orders2["order_status"].value_counts()

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:17.681818Z","iopub.execute_input":"2022-10-31T04:33:17.682133Z","iopub.status.idle":"2022-10-31T04:33:17.804324Z","shell.execute_reply.started":"2022-10-31T04:33:17.682103Z","shell.execute_reply":"2022-10-31T04:33:17.803269Z"}}
cust_orders = pd.merge(customers[["customer_id", "customer_unique_id"]], orders2[[
                       "customer_id", "order_purchase_timestamp", "order_id"]], on="customer_id", how="left")
cust_orders.shape

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:17.805431Z","iopub.execute_input":"2022-10-31T04:33:17.806013Z","iopub.status.idle":"2022-10-31T04:33:17.823202Z","shell.execute_reply.started":"2022-10-31T04:33:17.805982Z","shell.execute_reply":"2022-10-31T04:33:17.822018Z"}}
cust_orders

# %% [markdown]
# ## Customer never buy

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:17.825003Z","iopub.execute_input":"2022-10-31T04:33:17.825332Z","iopub.status.idle":"2022-10-31T04:33:17.874384Z","shell.execute_reply.started":"2022-10-31T04:33:17.825301Z","shell.execute_reply":"2022-10-31T04:33:17.873386Z"}}
cust_orders[cust_orders["order_purchase_timestamp"].isna()]

# %% [markdown]
# ## Customer buy

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:17.875644Z","iopub.execute_input":"2022-10-31T04:33:17.875967Z","iopub.status.idle":"2022-10-31T04:33:17.916549Z","shell.execute_reply.started":"2022-10-31T04:33:17.875936Z","shell.execute_reply":"2022-10-31T04:33:17.91543Z"}}
cust_orders_buy = cust_orders[~cust_orders["order_purchase_timestamp"].isna()]
cust_orders_buy

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:17.919665Z","iopub.execute_input":"2022-10-31T04:33:17.920048Z","iopub.status.idle":"2022-10-31T04:33:17.938911Z","shell.execute_reply.started":"2022-10-31T04:33:17.920013Z","shell.execute_reply":"2022-10-31T04:33:17.937811Z"}}
cust_orders_buy[cust_orders_buy["customer_id"]
                == "06b8999e2fba1a1fbc88172c00ba8bc7"]

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:17.940585Z","iopub.execute_input":"2022-10-31T04:33:17.941654Z","iopub.status.idle":"2022-10-31T04:33:17.95255Z","shell.execute_reply.started":"2022-10-31T04:33:17.94161Z","shell.execute_reply":"2022-10-31T04:33:17.9513Z"}}
cust_orders_buy["order_purchase_timestamp2"] = cust_orders_buy["order_purchase_timestamp"]

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:17.953842Z","iopub.execute_input":"2022-10-31T04:33:17.955054Z","iopub.status.idle":"2022-10-31T04:33:18.14194Z","shell.execute_reply.started":"2022-10-31T04:33:17.955019Z","shell.execute_reply":"2022-10-31T04:33:18.14077Z"}}
try2 = cust_orders_buy.groupby(["customer_unique_id"], as_index=False).agg({"customer_id": ["count"], "order_id": ["count"]
                                                                            })

try2.columns = list(map(''.join, try2.columns.values))

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:18.143757Z","iopub.execute_input":"2022-10-31T04:33:18.144424Z","iopub.status.idle":"2022-10-31T04:33:18.154729Z","shell.execute_reply.started":"2022-10-31T04:33:18.144378Z","shell.execute_reply":"2022-10-31T04:33:18.153899Z"}}
try2["order_idcount"].value_counts()

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:18.156282Z","iopub.execute_input":"2022-10-31T04:33:18.156992Z","iopub.status.idle":"2022-10-31T04:33:18.168796Z","shell.execute_reply.started":"2022-10-31T04:33:18.15695Z","shell.execute_reply":"2022-10-31T04:33:18.167628Z"}}
try2[try2["order_idcount"] > 1].shape

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:18.172057Z","iopub.execute_input":"2022-10-31T04:33:18.172376Z","iopub.status.idle":"2022-10-31T04:33:18.648775Z","shell.execute_reply.started":"2022-10-31T04:33:18.172347Z","shell.execute_reply":"2022-10-31T04:33:18.647924Z"}}
cust_orders_buy2 = cust_orders_buy.groupby(["customer_unique_id", "order_purchase_timestamp"], as_index=False).agg({"customer_id": ["count"], "order_id": ["count"]
                                                                                                                    })

cust_orders_buy2.columns = list(map(''.join, cust_orders_buy2.columns.values))

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:18.64982Z","iopub.execute_input":"2022-10-31T04:33:18.650888Z","iopub.status.idle":"2022-10-31T04:33:18.667116Z","shell.execute_reply.started":"2022-10-31T04:33:18.650841Z","shell.execute_reply":"2022-10-31T04:33:18.665767Z"}}
cust_orders_buy2

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:18.668569Z","iopub.execute_input":"2022-10-31T04:33:18.668983Z","iopub.status.idle":"2022-10-31T04:33:18.678048Z","shell.execute_reply.started":"2022-10-31T04:33:18.668953Z","shell.execute_reply":"2022-10-31T04:33:18.677046Z"}}
cust_orders_buy2["order_idcount"].value_counts()

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:18.679561Z","iopub.execute_input":"2022-10-31T04:33:18.679857Z","iopub.status.idle":"2022-10-31T04:33:18.698213Z","shell.execute_reply.started":"2022-10-31T04:33:18.679828Z","shell.execute_reply":"2022-10-31T04:33:18.69705Z"}}
cust_orders_buy2

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:18.699727Z","iopub.execute_input":"2022-10-31T04:33:18.700429Z","iopub.status.idle":"2022-10-31T04:33:18.741621Z","shell.execute_reply.started":"2022-10-31T04:33:18.700379Z","shell.execute_reply":"2022-10-31T04:33:18.740538Z"}}

cust_orders_buy2["order_purchase_timestamp"] = pd.to_datetime(
    cust_orders_buy2["order_purchase_timestamp"])
#

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:18.743119Z","iopub.execute_input":"2022-10-31T04:33:18.743471Z","iopub.status.idle":"2022-10-31T04:33:19.238375Z","shell.execute_reply.started":"2022-10-31T04:33:18.743438Z","shell.execute_reply":"2022-10-31T04:33:19.237538Z"}}
cust_orders_buy2['order_purchase_timestamp'] = cust_orders_buy2['order_purchase_timestamp'].dt.strftime(
    '%Y-%m')

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:19.2395Z","iopub.execute_input":"2022-10-31T04:33:19.240334Z","iopub.status.idle":"2022-10-31T04:33:19.248148Z","shell.execute_reply.started":"2022-10-31T04:33:19.240297Z","shell.execute_reply":"2022-10-31T04:33:19.246987Z"}}
cust_orders_buy2.dtypes

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:19.253884Z","iopub.execute_input":"2022-10-31T04:33:19.254215Z","iopub.status.idle":"2022-10-31T04:33:19.280225Z","shell.execute_reply.started":"2022-10-31T04:33:19.254187Z","shell.execute_reply":"2022-10-31T04:33:19.279254Z"}}
cust_orders_buy2["order_purchase_timestamp"] = pd.to_datetime(
    cust_orders_buy2["order_purchase_timestamp"])

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:19.281474Z","iopub.execute_input":"2022-10-31T04:33:19.281764Z","iopub.status.idle":"2022-10-31T04:33:19.296297Z","shell.execute_reply.started":"2022-10-31T04:33:19.281736Z","shell.execute_reply":"2022-10-31T04:33:19.295183Z"}}
cust_orders_buy2

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:19.297488Z","iopub.execute_input":"2022-10-31T04:33:19.297773Z","iopub.status.idle":"2022-10-31T04:33:19.316367Z","shell.execute_reply.started":"2022-10-31T04:33:19.297746Z","shell.execute_reply":"2022-10-31T04:33:19.315003Z"}}
cust_orders_buy2

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:19.317909Z","iopub.execute_input":"2022-10-31T04:33:19.318501Z","iopub.status.idle":"2022-10-31T04:33:37.093377Z","shell.execute_reply.started":"2022-10-31T04:33:19.31845Z","shell.execute_reply":"2022-10-31T04:33:37.092436Z"}}
size = cust_orders_buy2.shape[0]
#temp = pd.DataFrame(columns=['A'])
a = []
for i in range(size-1):
    if cust_orders_buy2.iloc[i, 0] == cust_orders_buy2.iloc[i+1, 0]:
        a.append(
            (cust_orders_buy2.iloc[i+1, 1] - cust_orders_buy2.iloc[i, 1])/np.timedelta64(1, 'M'))
    else:
        a.append(
            (cust_orders_buy2.iloc[i, 1] - cust_orders_buy2.iloc[i, 1])/np.timedelta64(1, 'M'))

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:37.094907Z","iopub.execute_input":"2022-10-31T04:33:37.095528Z","iopub.status.idle":"2022-10-31T04:33:37.118196Z","shell.execute_reply.started":"2022-10-31T04:33:37.095495Z","shell.execute_reply":"2022-10-31T04:33:37.117009Z"}}
diff = pd.DataFrame(a, columns=["diff"])
diff = round(diff)
diff.head()

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:37.11968Z","iopub.execute_input":"2022-10-31T04:33:37.120117Z","iopub.status.idle":"2022-10-31T04:33:37.141691Z","shell.execute_reply.started":"2022-10-31T04:33:37.120087Z","shell.execute_reply":"2022-10-31T04:33:37.140626Z"}}
cust_orders_buy3 = pd.concat([cust_orders_buy2, diff], axis=1)
cust_orders_buy3.tail(10)

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:37.143238Z","iopub.execute_input":"2022-10-31T04:33:37.143551Z","iopub.status.idle":"2022-10-31T04:33:37.160353Z","shell.execute_reply.started":"2022-10-31T04:33:37.143523Z","shell.execute_reply":"2022-10-31T04:33:37.159361Z"}}
cust_orders_buy3["diff"] = cust_orders_buy3["diff"].fillna(0)
cust_orders_buy3

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:37.161726Z","iopub.execute_input":"2022-10-31T04:33:37.162016Z","iopub.status.idle":"2022-10-31T04:33:37.182524Z","shell.execute_reply.started":"2022-10-31T04:33:37.161988Z","shell.execute_reply":"2022-10-31T04:33:37.181646Z"}}
cust_orders_buy3[((cust_orders_buy3["diff"] > 0) &
                  (cust_orders_buy3["diff"] <= 3))]

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:33:37.184146Z","iopub.execute_input":"2022-10-31T04:33:37.184759Z","iopub.status.idle":"2022-10-31T04:33:37.198205Z","shell.execute_reply.started":"2022-10-31T04:33:37.184715Z","shell.execute_reply":"2022-10-31T04:33:37.19704Z"}}
cust_orders_buy3.iloc[245:252]

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:44:56.574049Z","iopub.execute_input":"2022-10-31T04:44:56.574621Z","iopub.status.idle":"2022-10-31T04:44:58.235282Z","shell.execute_reply.started":"2022-10-31T04:44:56.574578Z","shell.execute_reply":"2022-10-31T04:44:58.234007Z"}}


def flags(df):
    if df["diff"] <= 0:
        return 1
    elif df["diff"] <= 3:
        return 0
    else:
        return 1


cust_orders_buy3["flagging"] = cust_orders_buy3.apply(flags, axis=1)


# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:44:58.236976Z","iopub.execute_input":"2022-10-31T04:44:58.237326Z","iopub.status.idle":"2022-10-31T04:44:58.247536Z","shell.execute_reply.started":"2022-10-31T04:44:58.237295Z","shell.execute_reply":"2022-10-31T04:44:58.246533Z"}}
cust_orders_buy3["flagging"].value_counts()

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:44:58.417071Z","iopub.execute_input":"2022-10-31T04:44:58.418174Z","iopub.status.idle":"2022-10-31T04:44:58.439014Z","shell.execute_reply.started":"2022-10-31T04:44:58.418117Z","shell.execute_reply":"2022-10-31T04:44:58.437718Z"}}
cust_orders_buy3

# %% [markdown]
# ## Getting Reviews

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:45:02.080504Z","iopub.execute_input":"2022-10-31T04:45:02.080934Z","iopub.status.idle":"2022-10-31T04:45:02.096297Z","shell.execute_reply.started":"2022-10-31T04:45:02.080898Z","shell.execute_reply":"2022-10-31T04:45:02.095074Z"}}
reviews.head()

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:45:02.201957Z","iopub.execute_input":"2022-10-31T04:45:02.202397Z","iopub.status.idle":"2022-10-31T04:45:02.218203Z","shell.execute_reply.started":"2022-10-31T04:45:02.202361Z","shell.execute_reply":"2022-10-31T04:45:02.217021Z"}}
orders.head()

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:45:02.334321Z","iopub.execute_input":"2022-10-31T04:45:02.335064Z","iopub.status.idle":"2022-10-31T04:45:02.450466Z","shell.execute_reply.started":"2022-10-31T04:45:02.335016Z","shell.execute_reply":"2022-10-31T04:45:02.449492Z"}}
orders_review = pd.merge(orders2[["customer_id", "order_purchase_timestamp", "order_id"]], reviews[[
                         "order_id", "review_score"]], on="order_id", how="left")
orders_review.shape

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:45:02.510819Z","iopub.execute_input":"2022-10-31T04:45:02.511472Z","iopub.status.idle":"2022-10-31T04:45:02.52872Z","shell.execute_reply.started":"2022-10-31T04:45:02.511423Z","shell.execute_reply":"2022-10-31T04:45:02.527409Z"}}
orders_review

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:45:02.665108Z","iopub.execute_input":"2022-10-31T04:45:02.665541Z","iopub.status.idle":"2022-10-31T04:45:02.682665Z","shell.execute_reply.started":"2022-10-31T04:45:02.665502Z","shell.execute_reply":"2022-10-31T04:45:02.681136Z"}}
customers

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:45:02.801135Z","iopub.execute_input":"2022-10-31T04:45:02.802281Z","iopub.status.idle":"2022-10-31T04:45:02.928017Z","shell.execute_reply.started":"2022-10-31T04:45:02.80224Z","shell.execute_reply":"2022-10-31T04:45:02.92685Z"}}
orders_review_cust = pd.merge(customers[["customer_id", "customer_unique_id"]], orders_review[[
                              "customer_id", "order_purchase_timestamp", "review_score"]], on="customer_id", how="left")
orders_review_cust.shape

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:45:02.991215Z","iopub.execute_input":"2022-10-31T04:45:02.991643Z","iopub.status.idle":"2022-10-31T04:45:03.009647Z","shell.execute_reply.started":"2022-10-31T04:45:02.991609Z","shell.execute_reply":"2022-10-31T04:45:03.008221Z"}}
orders_review_cust

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:45:03.111008Z","iopub.execute_input":"2022-10-31T04:45:03.111438Z","iopub.status.idle":"2022-10-31T04:45:03.526247Z","shell.execute_reply.started":"2022-10-31T04:45:03.111404Z","shell.execute_reply":"2022-10-31T04:45:03.525062Z"}}
orders_review_cust2 = orders_review_cust.groupby(["customer_unique_id", "order_purchase_timestamp"], as_index=False).agg({"review_score": ["min"]
                                                                                                                          })

orders_review_cust2.columns = list(
    map(''.join, orders_review_cust2.columns.values))

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:45:03.528278Z","iopub.execute_input":"2022-10-31T04:45:03.528643Z","iopub.status.idle":"2022-10-31T04:45:03.543818Z","shell.execute_reply.started":"2022-10-31T04:45:03.528612Z","shell.execute_reply":"2022-10-31T04:45:03.542562Z"}}
orders_review_cust2

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:45:03.545886Z","iopub.execute_input":"2022-10-31T04:45:03.546405Z","iopub.status.idle":"2022-10-31T04:45:04.082297Z","shell.execute_reply.started":"2022-10-31T04:45:03.546359Z","shell.execute_reply":"2022-10-31T04:45:04.081232Z"}}
orders_review_cust2["order_purchase_timestamp"] = pd.to_datetime(
    orders_review_cust2["order_purchase_timestamp"])
orders_review_cust2['order_purchase_timestamp'] = orders_review_cust2['order_purchase_timestamp'].dt.strftime(
    '%Y-%m')
orders_review_cust2["order_purchase_timestamp"] = pd.to_datetime(
    orders_review_cust2["order_purchase_timestamp"])


# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:45:04.084029Z","iopub.execute_input":"2022-10-31T04:45:04.084413Z","iopub.status.idle":"2022-10-31T04:45:04.101498Z","shell.execute_reply.started":"2022-10-31T04:45:04.084373Z","shell.execute_reply":"2022-10-31T04:45:04.100373Z"}}
orders_review_cust2

# %% [markdown]
# ## Getting Payment

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T05:11:22.222249Z","iopub.execute_input":"2022-10-31T05:11:22.223293Z","iopub.status.idle":"2022-10-31T05:11:22.246164Z","shell.execute_reply.started":"2022-10-31T05:11:22.223241Z","shell.execute_reply":"2022-10-31T05:11:22.244737Z"}}
payments

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T05:12:07.708027Z","iopub.execute_input":"2022-10-31T05:12:07.708491Z","iopub.status.idle":"2022-10-31T05:12:07.839637Z","shell.execute_reply.started":"2022-10-31T05:12:07.708454Z","shell.execute_reply":"2022-10-31T05:12:07.838059Z"}}
orders_payments = pd.merge(
    orders2[["customer_id", "order_purchase_timestamp", "order_id"]], payments, on="order_id", how="left")
orders_payments.shape

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T05:13:36.559062Z","iopub.execute_input":"2022-10-31T05:13:36.559556Z","iopub.status.idle":"2022-10-31T05:13:36.583566Z","shell.execute_reply.started":"2022-10-31T05:13:36.55952Z","shell.execute_reply":"2022-10-31T05:13:36.581574Z"}}
orders_payments

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T05:18:34.567817Z","iopub.execute_input":"2022-10-31T05:18:34.568275Z","iopub.status.idle":"2022-10-31T05:18:34.592226Z","shell.execute_reply.started":"2022-10-31T05:18:34.56824Z","shell.execute_reply":"2022-10-31T05:18:34.590908Z"}}
dummy = pd.get_dummies(orders_payments["payment_type"])
dummy

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T05:20:19.586532Z","iopub.execute_input":"2022-10-31T05:20:19.586967Z","iopub.status.idle":"2022-10-31T05:20:19.629375Z","shell.execute_reply.started":"2022-10-31T05:20:19.586935Z","shell.execute_reply":"2022-10-31T05:20:19.627901Z"}}
orders_payments2 = pd.concat([orders_payments[["customer_id", "order_purchase_timestamp",
                             "order_id", "payment_sequential", "payment_installments", "payment_value"]], dummy], axis=1)
orders_payments2

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T05:28:40.337825Z","iopub.execute_input":"2022-10-31T05:28:40.338261Z","iopub.status.idle":"2022-10-31T05:28:41.254621Z","shell.execute_reply.started":"2022-10-31T05:28:40.338227Z","shell.execute_reply":"2022-10-31T05:28:41.253253Z"}}
orders_payments3 = orders_payments2.groupby(["customer_id", "order_purchase_timestamp"], as_index=False).agg({
    "payment_sequential": ["max"], "payment_installments": ["mean"], "payment_value": ["sum"],
    "boleto": ["sum"], "credit_card": ["sum"], "debit_card": ["sum"], "voucher": ["sum"]
})

orders_payments3.columns = list(map(''.join, orders_payments3.columns.values))

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T05:28:41.25656Z","iopub.execute_input":"2022-10-31T05:28:41.256918Z","iopub.status.idle":"2022-10-31T05:28:41.281216Z","shell.execute_reply.started":"2022-10-31T05:28:41.256886Z","shell.execute_reply":"2022-10-31T05:28:41.279886Z"}}
orders_payments3

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T05:28:41.282805Z","iopub.execute_input":"2022-10-31T05:28:41.283175Z","iopub.status.idle":"2022-10-31T05:28:41.439701Z","shell.execute_reply.started":"2022-10-31T05:28:41.283142Z","shell.execute_reply":"2022-10-31T05:28:41.438473Z"}}
orders_payment_cust = pd.merge(
    customers[["customer_id", "customer_unique_id"]], orders_payments3, on="customer_id", how="left")
orders_payment_cust.shape

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T05:29:37.751908Z","iopub.execute_input":"2022-10-31T05:29:37.75245Z","iopub.status.idle":"2022-10-31T05:29:37.781114Z","shell.execute_reply.started":"2022-10-31T05:29:37.752408Z","shell.execute_reply":"2022-10-31T05:29:37.779567Z"}}
orders_payment_cust

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T05:30:53.032215Z","iopub.execute_input":"2022-10-31T05:30:53.033454Z","iopub.status.idle":"2022-10-31T05:30:53.827872Z","shell.execute_reply.started":"2022-10-31T05:30:53.033382Z","shell.execute_reply":"2022-10-31T05:30:53.826618Z"}}
orders_payment_cust2 = orders_payment_cust.groupby(["customer_unique_id", "order_purchase_timestamp"], as_index=False).agg({
    "payment_sequentialmax": ["max"], "payment_installmentsmean": ["mean"], "payment_valuesum": ["sum"],
    "boletosum": ["sum"], "credit_cardsum": ["sum"], "debit_cardsum": ["sum"], "vouchersum": ["sum"]
})

orders_payment_cust2.columns = list(
    map(''.join, orders_payment_cust2.columns.values))

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T05:30:55.865066Z","iopub.execute_input":"2022-10-31T05:30:55.865494Z","iopub.status.idle":"2022-10-31T05:30:55.892645Z","shell.execute_reply.started":"2022-10-31T05:30:55.86546Z","shell.execute_reply":"2022-10-31T05:30:55.891206Z"}}
orders_payment_cust2

# %% [markdown]
# ## Merging to one dataset

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:45:04.295151Z","iopub.execute_input":"2022-10-31T04:45:04.296129Z","iopub.status.idle":"2022-10-31T04:45:04.316159Z","shell.execute_reply.started":"2022-10-31T04:45:04.296089Z","shell.execute_reply":"2022-10-31T04:45:04.315077Z"}}
cust_orders_buy3

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:45:04.448831Z","iopub.execute_input":"2022-10-31T04:45:04.449223Z","iopub.status.idle":"2022-10-31T04:45:04.465308Z","shell.execute_reply.started":"2022-10-31T04:45:04.449192Z","shell.execute_reply":"2022-10-31T04:45:04.464278Z"}}
orders_review_cust2

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T05:31:16.681963Z","iopub.execute_input":"2022-10-31T05:31:16.682466Z","iopub.status.idle":"2022-10-31T05:31:16.709064Z","shell.execute_reply.started":"2022-10-31T05:31:16.68243Z","shell.execute_reply":"2022-10-31T05:31:16.707533Z"}}
orders_payment_cust2

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T05:31:47.118801Z","iopub.execute_input":"2022-10-31T05:31:47.119318Z","iopub.status.idle":"2022-10-31T05:31:47.127002Z","shell.execute_reply.started":"2022-10-31T05:31:47.119284Z","shell.execute_reply":"2022-10-31T05:31:47.125848Z"}}
orders_payment_cust2.columns

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T05:32:10.853302Z","iopub.execute_input":"2022-10-31T05:32:10.853841Z","iopub.status.idle":"2022-10-31T05:32:10.899826Z","shell.execute_reply.started":"2022-10-31T05:32:10.853803Z","shell.execute_reply":"2022-10-31T05:32:10.898437Z"}}
result1 = pd.concat([cust_orders_buy3, orders_review_cust2[["review_scoremin"]], orders_payment_cust2[['payment_sequentialmaxmax',
                    'payment_installmentsmeanmean', 'payment_valuesumsum', 'boletosumsum', 'credit_cardsumsum', 'debit_cardsumsum', 'vouchersumsum']]], axis=1)
result1

# %% [code]


# %% [markdown]
# ## Assestment features

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:45:04.820824Z","iopub.execute_input":"2022-10-31T04:45:04.821238Z","iopub.status.idle":"2022-10-31T04:45:04.892393Z","shell.execute_reply.started":"2022-10-31T04:45:04.821205Z","shell.execute_reply":"2022-10-31T04:45:04.891334Z"}}
a = pd.crosstab(result1["review_scoremin"],
                result1["flagging"], margins=True, margins_name="Total")
a

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:47:22.943086Z","iopub.execute_input":"2022-10-31T04:47:22.943609Z","iopub.status.idle":"2022-10-31T04:47:22.95348Z","shell.execute_reply.started":"2022-10-31T04:47:22.94357Z","shell.execute_reply":"2022-10-31T04:47:22.952208Z"}}


def nonevent(df):
    return (df[0]/964)


def event(df):
    return (df[1]/96231)


def Woe(df):
    return ln(df["%nonevent"]/df["%event"])


a["%nonevent"] = a.apply(nonevent, axis=1)
a["%event"] = a.apply(event, axis=1)


# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T04:47:23.908311Z","iopub.execute_input":"2022-10-31T04:47:23.909088Z","iopub.status.idle":"2022-10-31T04:47:23.922077Z","shell.execute_reply.started":"2022-10-31T04:47:23.909035Z","shell.execute_reply":"2022-10-31T04:47:23.920841Z"}}
a

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T05:07:31.69324Z","iopub.execute_input":"2022-10-31T05:07:31.693815Z","iopub.status.idle":"2022-10-31T05:07:31.70324Z","shell.execute_reply.started":"2022-10-31T05:07:31.693771Z","shell.execute_reply":"2022-10-31T05:07:31.701813Z"}}
a["WoE"] = np.log(a["%nonevent"]/a["%event"])

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T05:07:33.212363Z","iopub.execute_input":"2022-10-31T05:07:33.212781Z","iopub.status.idle":"2022-10-31T05:07:33.227779Z","shell.execute_reply.started":"2022-10-31T05:07:33.212748Z","shell.execute_reply":"2022-10-31T05:07:33.226391Z"}}
a

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T05:08:39.911489Z","iopub.execute_input":"2022-10-31T05:08:39.912034Z","iopub.status.idle":"2022-10-31T05:08:39.930939Z","shell.execute_reply.started":"2022-10-31T05:08:39.911994Z","shell.execute_reply":"2022-10-31T05:08:39.92937Z"}}
a["IV"] = (a["%nonevent"] - a["%event"])*a["WoE"]
a

# %% [code] {"execution":{"iopub.status.busy":"2022-10-31T05:09:02.713524Z","iopub.execute_input":"2022-10-31T05:09:02.714027Z","iopub.status.idle":"2022-10-31T05:09:02.723745Z","shell.execute_reply.started":"2022-10-31T05:09:02.713979Z","shell.execute_reply":"2022-10-31T05:09:02.722384Z"}}
a["IV"].sum()

# %% [code]
