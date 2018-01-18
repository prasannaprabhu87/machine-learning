package 'httpd' do
	action :install
end

file "/var/www/html/index.html" do
	content "<hello word>
	IP address is #{node['ipaddress']}
	hostname is #{node['hostname']}

"
end

service 'httpd' do
	action [:enable ,:start ]
end
