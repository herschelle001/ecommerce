### content of "create_user.py" file
from account.models import UserBase, Buyer, Seller

buyer_names = ['arun_LyuK3C', 'alice_A52pLv', 'bob_PEmb5S'] 
buyer_passwords = ['FNNuYBmUU6PmhP2F', 'hyagZDy5qJQnSAhC', 'nyVF5brZt8YCBtw6'] 
buyer_emails = ['popika4897@ecofreon.com', 'sdizcxuduzrywxfqpx@sdvrecft.com', 'glgltawqsnrpttauhf@sdvrecft.com']

seller_names = ['eve_z636LZ', 'feynmann_5hgNeS', '1st_year_books']
seller_passwords = ['9k8ZvKyhArfLNBrr', 'bkTdL2drYZEsML7C', 'DHeNTF6r67CsSkC9']
seller_emails = ['padebo5687@epeva.com', 'hiyduhudra@vusra.com', 'lozoduvy@onekisspresave.com']

"""

email, user name, name, password

---
echo "from account.models import UserBase; UserBase.objects.create_superuser('admin_FdaB9B@admin.com', 'admin_FdaB9B', 'admin_FdaB9B', '4e=ETw:=cVB2]%c#')" | python manage.py shell

echo "from account.models import UserBase; UserBase.objects.create_superuser('admin_HUP2au@admin.com', 'admin_HUP2au', 'admin_HUP2au', '57?:4J4#+Ew9e]E#')" | python manage.py shell

echo "from account.models import UserBase; UserBase.objects.create_superuser('admin_y9sSM4@admin.com', 'admin_y9sSM4', 'admin_y9sSM4', '26TJbYjBh}#{F~<')" | python manage.py shell

echo "from account.models import UserBase; UserBase.objects.create_superuser('admin_yJG2M2@admin.com', 'admin_yJG2M2', 'admin_yJG2M2', '}q%Jx.TaD3Ha-P9')" | python manage.py shell

echo "from account.models import UserBase; UserBase.objects.create_superuser('admin_8ebK8x@admin.com', 'admin_8ebK8x', 'admin_8ebK8x', 'w5y;X>jdcFu<DDDu')" | python manage.py shell
---

---
echo "from account.models import UserBase; UserBase.objects.create_superuser('admin_kcz6My@admin.com', 'admin_kcz6My', 'admin_kcz6My', 'z78~gqu]D.u<g_')" | python manage.py shell

echo "from account.models import UserBase; UserBase.objects.create_superuser('admin_G8fv3H@admin.com', 'admin_G8fv3H', 'admin_G8fv3H', ',?4?wY!7_5aa$k')" | python manage.py shell

echo "from account.models import UserBase; UserBase.objects.create_superuser('admin_SZrd9q@admin.com', 'admin_SZrd9q', 'admin_SZrd9q', ':+\[2>LHLjd6xn_')" | python manage.py shell

echo "from account.models import UserBase; UserBase.objects.create_superuser('admin_9y3LqW@admin.com', 'admin_9y3LqW', 'admin_9y3LqW', 'R>V;2YUgyKz&wd')" | python manage.py shell

echo "from account.models import UserBase; UserBase.objects.create_superuser('admin_jqjU2E@admin.com', 'admin_jqjU2E', 'admin_jqjU2E', 'fruft}N7B&V#3$A')" | python manage.py shell
---



"""