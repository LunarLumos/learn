অবশ্যই! আসুন **Stellarisys** Perl স্ক্রিপ্টের কাস্টম প্যাকেজগুলোকে বাংলায় বিস্তারিতভাবে ব্যাখ্যা করি।

---

## **Stellarisys-এ কাস্টম প্যাকেজগুলো**

### **1. LinkedList প্যাকেজ**
`LinkedList` প্যাকেজটি এলার্টগুলো সংরক্ষণের জন্য একটি লিঙ্কড লিস্ট স্ট্রাকচার ব্যবহার করে।

#### **কোড ব্যাখ্যা**
```perl
package LinkedList;
sub new       { bless { head => undef }, shift }
sub add       { my ($s, $d) = @_; $s->{head} = { data => $d, next => $s->{head} } }
sub show_all  { my $c = $_[0]->{head}; while ($c) { print $c->{data}; $c = $c->{next} } }
```

#### **উপাদানগুলো**
- **`package LinkedList;`**: একটি নতুন প্যাকেজ `LinkedList` সংজ্ঞায়িত করে।
- **`sub new { ... }`**: নতুন লিঙ্কড লিস্ট তৈরি করার জন্য কনস্ট্রাক্টর মেথড।
  - **`bless { head => undef }, shift`**: লিস্টটি `head` অ্যাট্রিবিউট দিয়ে শুরু করে, যা `undef` দিয়ে ইনিশিয়ালাইজ করা হয়, অর্থাৎ লিস্টটি খালি।

- **`sub add { ... }`**: লিঙ্কড লিস্টে একটি নতুন উপাদান যোগ করার মেথড।
  - **`my ($s, $d) = @_;`**: লিঙ্কড লিস্ট অবজেক্ট (`$s`) এবং যোগ করার ডেটা (`$d`) গ্রহণ করে।
  - **`$s->{head} = { data => $d, next => $s->{head} }`**: নতুন নোড তৈরি করে এবং তার `next` কে বর্তমান `head` এর দিকে নির্দেশ করে, ফলে এটি লিস্টের শুরুতে যুক্ত হয়।

- **`sub show_all { ... }`**: লিঙ্কড লিস্টের সব উপাদান প্রদর্শনের মেথড।
  - **`my $c = $_[0]->{head};`**: লিস্টের `head` থেকে শুরু করে।
  - **`while ($c) { ... }`**: লিস্টের শেষ পর্যন্ত প্রতিটি নোডের মধ্য দিয়ে লুপ করে।
  - **`print $c->{data};`**: বর্তমান নোডের ডেটা প্রিন্ট করে।
  - **`$c = $c->{next};`**: পরবর্তী নোডে চলে যায়।

### **2. Stack প্যাকেজ**
`Stack` প্যাকেজটি একটি স্ট্যাক ডেটা স্ট্রাকচার বাস্তবায়ন করে, যা লাস্ট ইন ফার্স্ট আউট (LIFO) নীতি অনুসরণ করে।

#### **কোড ব্যাখ্যা**
```perl
package Stack;
sub new       { bless { items => [] }, shift }
sub push      { push @{$_[0]->{items}}, $_[1] }
sub pop       { pop @{$_[0]->{items}} }
```

#### **উপাদানগুলো**
- **`package Stack;`**: একটি নতুন প্যাকেজ `Stack` সংজ্ঞায়িত করে।
- **`sub new { ... }`**: নতুন স্ট্যাক তৈরি করার জন্য কনস্ট্রাক্টর মেথড।
  - **`bless { items => [] }, shift`**: স্ট্যাকটি একটি খালি অ্যারে `items` দিয়ে ইনিশিয়ালাইজ করে।

- **`sub push { ... }`**: স্ট্যাকের শীর্ষে একটি আইটেম যোগ করার মেথড।
  - **`push @{$_[0]->{items}}, $_[1]`**: প্রদত্ত আইটেম (`$_[1]`) `items` অ্যারেতে যোগ করে।

- **`sub pop { ... }`**: স্ট্যাকের শীর্ষ থেকে একটি আইটেম মুছে ফেলার এবং ফেরত দেওয়ার মেথড।
  - **`pop @{$_[0]->{items}}`**: `items` অ্যারেতে থেকে শেষ আইটেমটি মুছে ফেলে এবং ফেরত দেয়।

### **3. Queue প্যাকেজ**
`Queue` প্যাকেজটি একটি কিউ ডেটা স্ট্রাকচার বাস্তবায়ন করে, যা ফার্স্ট ইন ফার্স্ট আউট (FIFO) নীতি অনুসরণ করে।

#### **কোড ব্যাখ্যা**
```perl
package Queue;
sub new       { bless { items => [] }, shift }
sub enqueue   { push @{$_[0]->{items}}, $_[1] }
sub dequeue   { shift @{$_[0]->{items}} }
sub size      { scalar @{$_[0]->{items}} }
```

#### **উপাদানগুলো**
- **`package Queue;`**: একটি নতুন প্যাকেজ `Queue` সংজ্ঞায়িত করে।
- **`sub new { ... }`**: নতুন কিউ তৈরি করার জন্য কনস্ট্রাক্টর মেথড।
  - **`bless { items => [] }, shift`**: কিউটি একটি খালি অ্যারে `items` দিয়ে ইনিশিয়ালাইজ করে।

- **`sub enqueue { ... }`**: কিউয়ের শেষে একটি আইটেম যোগ করার মেথড।
  - **`push @{$_[0]->{items}}, $_[1]`**: প্রদত্ত আইটেম (`$_[1]`) `items` অ্যারেতে যোগ করে।

- **`sub dequeue { ... }`**: কিউয়ের সামনে থেকে একটি আইটেম মুছে ফেলার এবং ফেরত দেওয়ার মেথড।
  - **`shift @{$_[0]->{items}}`**: `items` অ্যারেতে থেকে প্রথম আইটেমটি মুছে ফেলে এবং ফেরত দেয়।

- **`sub size { ... }`**: কিউয়ের মধ্যে আইটেমের সংখ্যা পাওয়ার মেথড।
  - **`scalar @{$_[0]->{items}}`**: `items` অ্যারেতে আইটেমের সংখ্যা ফেরত দেয়।

### **4. Graph প্যাকেজ**
`Graph` প্যাকেজটি একটি গ্রাফ ডেটা স্ট্রাকচার বাস্তবায়ন করে, যা নোডগুলোর (এক্ষেত্রে, IP ঠিকানাগুলোর) মধ্যে সংযোগগুলি উপস্থাপন করে।

#### **কোড ব্যাখ্যা**
```perl
package Graph;
sub new            { bless { nodes => {} }, shift }
sub add_connection { my ($s, $u, $v) = @_; $s->{nodes}{$u}{$v} = $s->{nodes}{$v}{$u} = 1 }
sub print_graph    { my $s = shift; while (my ($n, $e) = each %{$s->{nodes}}) {
                        print "$n -> ", join(', ', keys %$e), "\n";
                    }}
```

#### **উপাদানগুলো**
- **`package Graph;`**: একটি নতুন প্যাকেজ `Graph` সংজ্ঞায়িত করে।
- **`sub new { ... }`**: নতুন গ্রাফ তৈরি করার জন্য কনস্ট্রাক্টর মেথড।
  - **`bless { nodes => {} }, shift`**: গ্রাফটি একটি হ্যাশ `nodes` দিয়ে ইনিশিয়ালাইজ করে, যা সংযোগগুলি ধারণ করে।

- **`sub add_connection { ... }`**: দুটি নোডের মধ্যে সংযোগ যোগ করার মেথড।
  - **`my ($s, $u, $v) = @_;`**: গ্রাফ অবজেক্ট (`$s`) এবং দুটি নোড (`$u` এবং `$v`) গ্রহণ করে।
  - **`$s->{nodes}{$u}{$v} = $s->{nodes}{$v}{$u} = 1;`**: নোড `u` এবং `v` এর মধ্যে দ্বিমুখী সংযোগ তৈরি করে।

- **`sub print_graph { ... }`**: গ্রাফের সংযোগগুলি প্রিন্ট করার মেথড।
  - **`my $s = shift;`**: গ্রাফ অবজেক্ট গ্রহণ করে।
  - **`while (my ($n, $e) = each %{$s->{nodes}}) { ... }`**: প্রতিটি নোড এবং তার এজগুলোর মধ্য দিয়ে লুপ করে।
  - **`print "$n -> ", join(', ', keys %$e), "\n";`**: নোড এবং তার সংযুক্ত নোডগুলো প্রিন্ট করে।

### **5. BST (Binary Search Tree) প্যাকেজ**
`BST` প্যাকেজটি একটি বাইনারি সার্চ ট্রি বাস্তবায়ন করে, যা ইউনিক IP ঠিকানাগুলো সংরক্ষণ করে।

#### **কোড ব্যাখ্যা**
```perl
package BST;
sub new     { bless { root => undef }, shift }
sub insert  {
    my ($s, $v) = @_;
    my $n = \$s->{root};
    while ($$n) {
        $n = $v lt $$n->{value} ? \$$n->{left} : \$$n->{right};
    }
    $$n = { value => $v, left => undef, right => undef };
}
sub inorder {
    my $s = shift;
    my (@stack, $c) = ();
    $c = $s->{root};
    while (@stack || defined $c) {
        if (defined $c) {
            push @stack, $c;
            $c = $c->{left};
        } else {
            $c = pop @stack;
            print $c->{value}, "\n";
            $c = $c->{right};
        }
    }
}
```

#### **উপাদানগুলো**
- **`package BST;`**: একটি নতুন প্যাকেজ `BST` সংজ্ঞায়িত করে।
- **`sub new { ... }`**: নতুন বাইনারি সার্চ ট্রি তৈরি করার জন্য কনস্ট্রাক্টর মেথড।
  - **`bless { root => undef }, shift`**: ট্রিটি একটি `root` অ্যাট্রিবিউট দিয়ে ইনিশিয়ালাইজ করে, যা `undef`।

- **`sub insert { ... }`**: একটি মান বাইনারি সার্চ ট্রিতে যোগ করার মেথড।
  - **`my ($s, $v) = @_;`**: BST অবজেক্ট (`$s`) এবং যোগ করার মান (`$v`) গ্রহণ করে।
  - **`my $n = \$s->{root};`**: ট্রির রুট থেকে শুরু করে।
  - **`while ($$n) { ... }`**: নতুন মানের জন্য একটি খালি স্থান খুঁজে বের করার জন্য লুপ করে।
    - **`$n = $v lt $$n->{value} ? \$$n->{left} : \$$n->{right};`**: মানের তুলনা করে বাম বা ডানে যেতে সিদ্ধান্ত নেয়।
  - **`$$n = { value => $v, left => undef, right => undef };`**: নতুন নোড তৈরি করে এবং তার সন্তানগুলোকে `undef` সেট করে।

- **`sub inorder { ... }`**: বাইনারি সার্চ ট্রির ইন-অর্ডার ট্রাভার্সাল করার মেথড।
  - **`my $s = shift;`**: BST অবজেক্ট গ্রহণ করে।
  - **`my (@stack, $c) = ();`**: একটি স্ট্যাক এবং একটি বর্তমান নোড ভেরিয়েবল ইনিশিয়ালাইজ করে।
  - **`$c = $s->{root};`**: ট্রির রুট থেকে শুরু করে।
  - **`while (@stack || defined $c) { ... }`**: স্ট্যাক খালি না হওয়া এবং বর্তমান নোড `undefined` না হওয়া পর্যন্ত লুপ করে।
    - **`if (defined $c) { ... }`**: যদি বর্তমান নোড `defined` হয়, তাহলে এটি স্ট্যাকে যোগ করে এবং বামে চলে যায়।
    - **`else { ... }`**: যদি বর্তমান নোড `undefined` হয়, তাহলে স্ট্যাক থেকে পপ করে, মান প্রিন্ট করে এবং ডানে চলে যায়।

---

## **উপসংহার**
এই কাস্টম প্যাকেজগুলো **Stellarisys** টুলের জন্য অপরিহার্য ডেটা স্ট্রাকচার প্রদান করে, যা এলার্টগুলো কার্যকরভাবে পরিচালনা করতে, সংযোগগুলো ট্র্যাক করতে এবং ইউনিক IP ঠিকানাগুলো সংরক্ষণ করতে সক্ষম। এই প্যাকেজগুলো বুঝতে পারলে আপনি টুলটি কিভাবে লগ ডেটা প্রক্রিয়া করে এবং সম্ভাব্য নিরাপত্তা হুমকি সনাক্ত করে তা grasp করতে পারবেন। যদি আপনার কোনো নির্দিষ্ট প্রশ্ন থাকে বা কোনো অংশ সম্পর্কে আরও ব্যাখ্যা প্রয়োজন হয়, তাহলে নির্দ্বিধায় জিজ্ঞাসা করুন!
Sure! Here’s a comprehensive A to Z breakdown of the **Stellarisys** tool's process, detailing each step from start to finish in a clear and structured manner, using an algorithmic approach.

---

## **A to Z Process of Stellarisys Tool**

### **A. Start**
- Begin the execution of the script.

### **B. Command-Line Options Handling**
1. **Parse Command-Line Arguments**:
   - Check for the help flag (`-h` or `--help`):
     - If present, display the help message and exit.
   - Check for the log file option (`-l <file>`):
     - If provided, set the variable `logfile` to the specified file name.
   - Check for the output file option (`-o <file>`):
     - If provided, set the variable `outfile` to the specified file name.

### **C. Log Data Acquisition**
2. **Read Log Data**:
   - If `logfile` is defined:
     - Open the file and read all lines into an array called `lines[]`.
     - Close the file after reading.
   - If `logfile` is not defined:
     - Check for standard input.
     - If standard input is not available, print an error message and exit.
     - If available, read all lines from standard input into `lines[]`.

### **D. Data Structures Initialization**
3. **Initialize Data Structures**:
   - Create a new instance of `LinkedList` to store alerts.
   - Create a new instance of `Queue` to track login requests.
   - Create a new instance of `Graph` to represent connections between IP addresses.
   - Create a new instance of `Binary Search Tree (BST)` to store unique IP addresses.

### **E. Attack Patterns Definition**
4. **Define Attack Patterns**:
   - Create an array of attack patterns, each containing:
     - A name (e.g., "SQL_INJECTION").
     - A regex pattern to match the attack.
     - A color code for formatting alerts.

### **F. Log Analysis Loop**
5. **Analyze Each Log Line**:
   - For each line in `lines[]`:
     - Remove any trailing newline characters.
     - Extract the IP address from the line.
     - Initialize a flag `t_found` to false (indicating no attack found yet).
     - Insert the extracted IP address into the BST.
     - If there is a previous IP address (`last_ip`), add a connection in the Graph.
     - Update `last_ip` to the current IP address.

### **G. Attack Detection**
6. **Check for Attack Patterns**:
   - For each attack pattern in the defined patterns:
     - Check if the current line matches the attack pattern using regex.
     - If a match is found:
       - Construct an alert message.
       - Print the alert message to the console.
       - Add the alert to the LinkedList.
       - Send the alert to Telegram.
       - Set `t_found` to true and break out of the loop.

### **H. Brute Force Detection**
7. **Detect Brute Force Attempts**:
   - If the line contains "login.php":
     - Enqueue the line into the Queue.
     - If the size of the Queue exceeds a predefined threshold (e.g., 5):
       - Dequeue the oldest request from the Queue.
       - Construct a brute force alert message.
       - Print the brute force alert message to the console.
       - Add the brute force alert to the LinkedList.
       - Send the brute force alert to Telegram.
       - Set `t_found` to true.

### **I. Safe Line Output**
8. **Print Safe Lines**:
   - If no attack was detected (`t_found` is false):
     - Print the line as "SAFE".

### **J. Summary Output**
9. **Print Summary of Alerts**:
   - After processing all lines, print a summary header.
   - Call the `show_all` method of the LinkedList to print all stored alerts.
   - Print a summary footer.

### **K. End**
10. **Conclude Execution**:
    - The tool finishes execution, providing the user with a comprehensive overview of detected security threats.

---

## **Example Scenario**
1. **Execution**: You run the tool with a command like:
   ```bash
   perl stellarisys.pl -l server_logs.txt
   ```
2. **Processing**: The tool reads the log file, analyzes each line for attack patterns, and detects any suspicious activity.
3. **Alerts**: If an SQL injection is detected, an alert is generated, printed, and sent to your Telegram.
4. **Summary**: After processing, the tool provides a summary of all alerts detected during the analysis.

---

This A to Z breakdown provides a clear and structured overview of how the **Stellarisys** tool operates, detailing the steps taken to analyze log data and manage alerts in a straightforward manner. If you have any further questions or need clarification on specific parts, feel free to ask!
