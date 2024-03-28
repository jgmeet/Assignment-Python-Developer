
def sort_data(data, K):
    return sorted(data, key=lambda x: x[K])

def main():

    inputs = input()
    N, M = map(int, inputs.split())

    data = []
    for i in range(N):
        input_atrributes = input()
        attributes = list(map(int, input_atrributes.split()))
        data.append(attributes)

    K = int(input())

    # Sort data based on Kth attribute
    sorted_data = sort_data(data, K)

    print("Sorted data by Kth attribute:")
    for row in sorted_data:
        print(*row)
        
if __name__ == '__main__':
    main()
