import csv


def convert_fairdeal_data(input_data):
    # Parse the input data into a Python data structure
    customers = []
    for row in input_data:
        name = row['name']
        email = row['email']
        phone = row['phone']
        address = row['address']
        customer = {'name': name, 'email': email,
                    'phone': phone, 'address': address}
        customers.append(customer)

    # Convert the data structure into the desired output format
    output_data = []
    for customer in customers:
        name = customer['name']
        email = customer['email']
        phone = customer['phone']
        address = customer['address']
        output_data.append({'Name': name, 'Email': email,
                           'Phone': phone, 'Address': address})

    return output_data


def main():
    # Read in the input data
    with open('fairdeal_customers.csv', 'r') as f:
        reader = csv.DictReader(f)
        input_data = list(reader)

    # Convert the data
    output_data = convert_fairdeal_data(input_data)

    # Write the output data to a file
    with open('goodskart_customers.csv', 'w') as f:
        fieldnames = ['Name', 'Email', 'Phone', 'Address']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in output_data:
            writer.writerow(row)


if __name__ == '__main__':
    main()
