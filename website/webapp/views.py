from django.shortcuts import render,redirect
from datetime import datetime
from .models import Notice,User_details,Complain_table,House_holding_number
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


# Create your views here.
def home(request):
	notice_count = Notice.objects.all().count()
	register_user_count= User.objects.count()
	complain_count = Complain_table.objects.all().count()
	context={
		'date':datetime.date(datetime.now()),
		'time':datetime.time(datetime.now()),
		'notice':notice_count,
		'user_count':register_user_count,
		'complain_count':complain_count,
	}
	return render(request,'webapp/home.html',context)

def details(request):
	return render(request,'webapp/details.html')

@login_required(login_url='/login/')
def information(request):
	notice = Notice.objects.all()
	your_complain=Complain_table.objects.filter(complainer_name=request.user)
	context={
		'notices':notice,
		'complains':your_complain,
	}
	return render(request,'webapp/notice.html',context)

def login(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']

		user=auth.authenticate(username=username,password=password)

		if user is not None:
			if user.is_staff:
				auth.login(request,user)
				return redirect('adminpage')
			else:
				auth.login(request,user)
				return redirect('information')
		else:
			messages.info(request,"Invalid Username and Password")
			return render(request,'webapp/login.html')

	else:
		return render(request,'webapp/login.html')

def register(request):
	if request.method=='POST':
		username=request.POST['username']
		firstname=request.POST['first_name']
		lastname=request.POST['last_name']
		email=request.POST['your_email']
		password=request.POST['password']
		confirmpassword=request.POST['comfirm_password']
		postal_code=request.POST['postalcode']
		address1=request.POST['address']

		if password==confirmpassword:
			if User.objects.filter(username=username).exists():
				messages.info(request,"Username Token!!!")
				return render(request,'webapp/register.html')

			elif User.objects.filter(email=email).exists():
				messages.info(request,"Email Token!!!")
				return render(request,'webapp/register.html')

			else:
				user=User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
				userdetails=User_details(postalcode=postal_code,address=address1)
				userdetails.user=user
				user.save()
				userdetails.save()
			    
				messages.warning(request, "Registration Completed!!!")

				return render(request,'webapp/register.html')
		else:
			messages.warning(request, "Password didn't matched!!!")
			return render(request,'webapp/register.html')

	else:
		return render(request,'webapp/register.html')


def logout(request):
	auth.logout(request)
	return redirect('index')

def fpass(request):
	if request.method=='POST':
		username=request.POST['username']
		email=request.POST['email']
		newpassword=request.POST['password2']

		user=User.objects.get(username=username)

		if user is not None:
			if email==user.email:
				user.set_password(newpassword)
				user.save()
				messages.info(request,"Password changed")
				return render(request,'webapp/change_user_pass.html')
			else:
				messages.info(request,"Email didnot matched!!!")
				return render(request,'webapp/change_user_pass.html')
		else:
			messages.info(request,"User didnot registered!!!")
			return render(request,'webapp/change_user_pass.html')



	else:
		return render(request,'webapp/change_user_pass.html')

@login_required(login_url='/login/')
def adminpage(request):
		if request.user.is_staff:
			if request.method=='POST':
				subject=request.POST['subject']
				description=request.POST['description']

				notice=Notice(subject=subject,description=description,dateshow=datetime.date(datetime.now()))
				notice.save()
				messages.info(request,"New Notice Added!!!")
				notice_count = Notice.objects.all().count()
				complain_count = Complain_table.objects.all().count()
				register_user_count= User.objects.count()
				notice = Notice.objects.all()
				complains=Complain_table.objects.all()
				household=House_holding_number.objects.all().count()
				context={
					'complains_count':complain_count,
					'notice':notice_count,
					'usercount':register_user_count,
					'notices':notice,
					'complains':complains,
					'holding_no':household,
				}
				return render(request,'webapp/adminpage.html',context)

			else:
				notice_count = Notice.objects.all().count()
				complain_count = Complain_table.objects.all().count()
				register_user_count= User.objects.count()
				notice = Notice.objects.all()
				complains=Complain_table.objects.all()
				household=House_holding_number.objects.all().count()
				context={
					'complains_count':complain_count,
					'notice':notice_count,
					'usercount':register_user_count,
					'notices':notice,
					'complains':complains,
					'holding_no':household,
				}
				return render(request,'webapp/adminpage.html',context)
		else:
			messages.info(request,"Your are not authorized to login as ADMIN.")
			return redirect('information')
		

@login_required(login_url='/login/')
def complain(request):
	if request.method=='POST':
		name=request.POST['name']
		email=request.POST['email']
		phone_number=request.POST['phone-number']
		area_name=request.POST['area']
		area_code=request.POST['pincode']
		holding_no=request.POST['holdingno']
		subject=request.POST['comoplainsubject']
		complainm=request.POST['complainmsg']
		

		if bool(request.FILES.get('photo', False)) == True:
			if House_holding_number.objects.filter(holding_number=holding_no).exists():
				complain=Complain_table(complainer_name=name,complainer_email=email,complainer_phone_number=phone_number,complaint_area_name=
					area_name,complaint_postal_code=area_code,house_holdin_number=holding_no,complain_subject=subject,
					complain=complainm,image_field=request.FILES['photo'],dateshow=datetime.date(datetime.now()),timeshow=datetime.time(datetime.now().replace(second=0, microsecond=0)))
				complain.save()
				messages.info(request,"Complain saved!!!")
				return redirect('information')
			else:
				messages.info(request,"You are not under this Municipal Corporation.Please contact with your Municipal Authority.")
				return redirect('complain')
		else:
			messages.info(request,"You forget to add image!!!")
			return redirect('complain')


	else:
		return render(request,'webapp/complain.html')