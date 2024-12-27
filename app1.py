import timeit
from flask import Flask, request, jsonify, render_template
from exponential_search import exponential_search, exponential_search_wrapper
from binary_search import binary_search, binary_search_wrapper
from interpolation_test import interpolation_search, interpolation_search_wrapper
from jump_search import jump_search, jump_search_wrapper
from linear_search import linear_search, linear_search_wrapper
from ternary_search import ternary_search, ternary_search_wrapper
from dq import Node, Queue, Deque
import random
from infix_postfix_conversion import infix_to_postfix, Stack


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile')
def profile():
    return render_template('group_profile.html')


@app.route('/works', methods=['GET', 'POST'])
def works():
    return render_template('works.html')


@app.route('/contact')
def contact():
    return render_template('contacts.html')


@app.route('/work1', methods=['GET', 'POST'])
def work1():
    return render_template('work1.html')


@app.route('/work2', methods=['GET', 'POST'])
def work2():
    return render_template('work2.html')


@app.route('/work3', methods=['GET', 'POST'])
def work3():
    return render_template('work3.html')


@app.route('/work4', methods=['GET', 'POST'])
def work4():
    return render_template('work4.html')


@app.route('/work5', methods=['GET', 'POST'])
def work5():
    return render_template('work5.html')


@app.route('/work6', methods=['GET', 'POST'])
def work6():
    return render_template('work6.html')


@app.route('/bubble')
def bubble():
    return render_template('bubblesortalgo.html')


@app.route('/bubblesort')
def bubble_sort():
    return render_template('bubblesort.html')


@app.route('/bubblesort2')
def bubble_sort2():
    return render_template('bubblesort2.html')


@app.route('/results')
def results():
    return render_template('results.html')


@app.route("/smallalgo", methods=["GET", "POST"])
def small_algo():
    
    numbers = range(1, 101)
    test_data = ", ".join(map(str, numbers))
    if request.method == "POST":
        array_str = request.form.get("array")
        target_str = request.form.get("target")
        search_type = request.form.get("search_type")

        try:
            array = list(map(int, array_str.split(",")))
            target = int(target_str)
            low, high = 0, len(array) - 1

            result = -1  # Initialize result before the conditional statements

            if search_type == "exponential":
                execution_time = timeit.timeit("exponential_search_wrapper(exponential_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = exponential_search_wrapper(binary_search, array, target)
                # result = exponential_search(array, target)
            elif search_type == "binary":
                execution_time = timeit.timeit("binary_search_wrapper(binary_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = binary_search_wrapper(binary_search, array, target)
            elif search_type == "interpolation":
                execution_time = timeit.timeit("interpolation_search_wrapper(interpolation_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = interpolation_search_wrapper(interpolation_search, array, target)                
                # result = interpolation_search(array, target)
            elif search_type == "jump":
                execution_time = timeit.timeit("jump_search_wrapper(jump_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = jump_search_wrapper(interpolation_search, array, target)  
                # result = jump_search(array, target)
            elif search_type == "linear":
                execution_time = timeit.timeit("linear_search_wrapper(linear_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = linear_search_wrapper(linear_search, array, target)  
                # result = linear_search(array, target)
            elif search_type == "ternary":
                execution_time = timeit.timeit("ternary_search_wrapper(ternary_search, array, target, low, high)",
                                               globals={**globals(), "array": array, "target": target, "low": low, "high": high}, number=1) * 1000
                result = ternary_search_wrapper(ternary_search, array, target, low, high)  
                # result = ternary_search(array, target, low, high)

            return render_template("search_algo.html", result=result, search_type=search_type, execution_time=execution_time,
                                   test_data=test_data)
        except ValueError:
            return render_template("search_algo.html", error="Invalid input. Ensure the array and target are integers.")
    return render_template("search_algo.html",test_data=test_data)


@app.route("/mediumalgo", methods=["GET", "POST"])
def medium_algo():
    
    numbers = range(1, 1001)
    test_data = ", ".join(map(str, numbers))
    if request.method == "POST":
        array_str = request.form.get("array")
        target_str = request.form.get("target")
        search_type = request.form.get("search_type")

        try:
            array = list(map(int, array_str.split(",")))
            target = int(target_str)
            low, high = 0, len(array) - 1

            result = -1  # Initialize result before the conditional statements

            if search_type == "exponential":
                execution_time = timeit.timeit("exponential_search_wrapper(exponential_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = exponential_search_wrapper(binary_search, array, target)
                # result = exponential_search(array, target)
            elif search_type == "binary":
                execution_time = timeit.timeit("binary_search_wrapper(binary_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = binary_search_wrapper(binary_search, array, target)
            elif search_type == "interpolation":
                execution_time = timeit.timeit("interpolation_search_wrapper(interpolation_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = interpolation_search_wrapper(interpolation_search, array, target)                
                # result = interpolation_search(array, target)
            elif search_type == "jump":
                execution_time = timeit.timeit("jump_search_wrapper(jump_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = jump_search_wrapper(interpolation_search, array, target)  
                # result = jump_search(array, target)
            elif search_type == "linear":
                execution_time = timeit.timeit("linear_search_wrapper(linear_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = linear_search_wrapper(linear_search, array, target)  
                # result = linear_search(array, target)
            elif search_type == "ternary":
                execution_time = timeit.timeit("ternary_search_wrapper(ternary_search, array, target, low, high)",
                                               globals={**globals(), "array": array, "target": target, "low": low, "high": high}, number=1)  * 1000
                result = ternary_search_wrapper(ternary_search, array, target, low, high)  
                # result = ternary_search(array, target, low, high)

            return render_template("search_algo.html", result=result, search_type=search_type, execution_time=execution_time,
                                   test_data=test_data)
        except ValueError:
            return render_template("search_algo.html", error="Invalid input. Ensure the array and target are integers.")
    return render_template("search_algo.html",test_data=test_data)


@app.route("/largealgo", methods=["GET", "POST"])
def large_algo():
    
    numbers = range(1, 10001)
    test_data = ", ".join(map(str, numbers))
    if request.method == "POST":
        array_str = request.form.get("array")
        target_str = request.form.get("target")
        search_type = request.form.get("search_type")

        try:
            array = list(map(int, array_str.split(",")))
            target = int(target_str)
            low, high = 0, len(array) - 1

            result = -1  # Initialize result before the conditional statements

            if search_type == "exponential":
                execution_time = timeit.timeit("exponential_search_wrapper(exponential_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = exponential_search_wrapper(binary_search, array, target)
                # result = exponential_search(array, target)
            elif search_type == "binary":
                execution_time = timeit.timeit("binary_search_wrapper(binary_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = binary_search_wrapper(binary_search, array, target)
            elif search_type == "interpolation":
                execution_time = timeit.timeit("interpolation_search_wrapper(interpolation_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = interpolation_search_wrapper(interpolation_search, array, target)                
                # result = interpolation_search(array, target)
            elif search_type == "jump":
                execution_time = timeit.timeit("jump_search_wrapper(jump_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = jump_search_wrapper(interpolation_search, array, target)  
                # result = jump_search(array, target)
            elif search_type == "linear":
                execution_time = timeit.timeit("linear_search_wrapper(linear_search, array, target)",
                                               globals={**globals(), "array": array, "target": target}, number=1) * 1000
                result = linear_search_wrapper(linear_search, array, target)  
                # result = linear_search(array, target)
            elif search_type == "ternary":
                execution_time = timeit.timeit("ternary_search_wrapper(ternary_search, array, target, low, high)",
                                               globals={**globals(), "array": array, "target": target, "low": low, "high": high}, number=1) * 1000
                result = ternary_search_wrapper(ternary_search, array, target, low, high)  
                # result = ternary_search(array, target, low, high)

            return render_template("search_algo.html", result=result, search_type=search_type, execution_time=execution_time,
                                   test_data=test_data)
        except ValueError:
            return render_template("search_algo.html", error="Invalid input. Ensure the array and target are integers.")
    return render_template("search_algo.html",test_data=test_data)


@app.route("/search", methods=["POST"])
def search():
    data = request.get_json()

    if not data or "array" not in data or "target" not in data:
        return jsonify({"error": "Invalid request data. Provide 'array' and 'target'."}), 400

    array = data["array"]
    target = data["target"]

    result_iterative = exponential_search(array, target)

    return jsonify({
        "iterative_search_result": result_iterative,
    })


@app.route('/infix-postfix', methods=['GET', 'POST'])
def infix():
    result = None
    if request.method == 'POST':
        infix_notation = request.form.get('infix', '')
        postfix = infix_to_postfix(infix_notation)

        steps = ""

        for i in range(len(postfix) + 1):
            steps += (''.join(postfix[:i]) + "\n")

        result = f"Processed Conversion: {steps}\nOutput Postfix: \n{postfix}"

    return render_template('infixpostfix.html', result=result)


global_queue = Queue()
@app.route("/queue", methods=["GET", "POST"])
def queue():
    global global_queue
    linked_list_data = []

    if request.method == "POST":
        usage = request.form.get("usage")

        if usage == "enqueue":
            data_to_add = request.form.get("data")
            global_queue.enqueue(data_to_add)
            linked_list_data = global_queue.printLinkedList()
            print("Linked List Data:", linked_list_data)

        elif usage == "dequeue":
            global_queue.dequeue()
            linked_list_data = global_queue.printLinkedList()
            print("Linked List Data:", linked_list_data)
    return render_template("Queue.html", linked_list_data=linked_list_data)



global_deque = Deque()
@app.route("/deque", methods=["GET", "POST"])
def deque():
    global global_deque
    linked_list_data = []

    if request.method == "POST":
        usage = request.form.get("usage")

        if usage == "add front":
            data_to_add = request.form.get("data")
            global_deque.add_front(data_to_add)
            linked_list_data = global_deque.printLinkedList()
            print("Linked List Data:", linked_list_data)


        elif usage == "add rear":
            data_to_add = request.form.get("data")
            global_deque.add_rear(data_to_add)
            linked_list_data = global_deque.printLinkedList()
            print("Linked List Data:", linked_list_data)


        elif usage == "remove front":
            global_deque.remove_front()
            linked_list_data = global_deque.printLinkedList()
            print("Linked List Data:", linked_list_data)


        elif usage == "remove rear":
            global_deque.remove_rear()
            linked_list_data = global_deque.printLinkedList()
            print("Linked List Data:", linked_list_data)




    return render_template("Deque.html", linked_list_data=linked_list_data)





if __name__ == "__main__":
    app.run(debug=True)
