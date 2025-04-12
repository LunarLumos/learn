
---

## 🅰️ **Part A – HTML (30 Marks)**

### **Task A**

---

### **1. Ensuring the website follows web design principles – [5 Marks]**

When designing the Sultan's Dine website, I made sure to follow the key principles of good web design: **clarity, consistency, simplicity, and accessibility**.

The layout is structured into clean, meaningful sections such as the hero area, about, menu, gallery, reviews, and contact. I used semantic HTML tags like `<section>`, `<header>`, and `<footer>` which help with both readability and accessibility. The `.header` is fixed at the top of the page and includes a navigation bar (`.navbar-list`) with anchor links that allow users to scroll smoothly to each section. This makes the user journey straightforward and intuitive.

The design is kept consistent by using a shared `.container` class for width control and spacing throughout the website. For example, in the `.about`, `.gallery`, and `.contact-form` sections, the container keeps all content aligned and visually balanced.

I also included accessibility features like `alt` attributes on all images, easy-to-read fonts from Google Fonts (`Poppins` and `Playfair Display`), and enough contrast between background and text colors using custom variables like `--primary`, `--secondary`, and `--white`. These help all users—including those with visual impairments—navigate and understand the content more easily.

---

### **2. Designing for standard desktop screen resolutions – [5 Marks]**

To make sure my website works well on all standard desktop screen resolutions (like 1366x768 or 1920x1080), I structured it using the `.container` class, which sets a `max-width` and auto margin so that the content stays centered and doesn't stretch across the full width of the screen.

I also used modern CSS layout systems like **Flexbox** and **CSS Grid** in various sections such as `.team-grid`, `.menu-grid`, and `.gallery-grid`. These allow items to adjust and wrap naturally without causing overflow. As a result, even if the user resizes their browser window, the content reflows properly.

On top of that, I applied **media queries** that adjust styles at breakpoints like 992px, 768px, and 576px. This ensures that the design adapts well to tablet and mobile views without introducing horizontal scrollbars.

For example, the two-column layout of `.about .container` becomes a single column on smaller screens, and the `.navbar-list` collapses into a toggleable menu on mobile, thanks to the `.nav-toggle` button. I tested the site on different devices and screen sizes to ensure the content was always visible and well-aligned without the need to scroll sideways.

---

### **3. Creating a structured and diverse input form – [5 Marks]**

In the contact section, I created a form inside a `.contact-form` layout. The goal was to collect user information in an organized, clear, and professional way.

The form includes multiple types of inputs:
- **Text fields** for user name and phone number.
- An **email field** that validates proper email format.
- A **dropdown menu** (`<select>`) so users can choose the type of event (like Wedding or Corporate).
- A **date input** to pick the event date.
- A **number field** to enter the number of guests.
- A **textarea** for any additional notes or special requests.
- Finally, a **submit button** styled using the `.btn` class.

I added the `required` attribute to all critical fields to prevent incomplete submissions, and also wrote JavaScript form validation. It checks that name, email, phone number, and date are correctly filled before allowing submission.

All inputs are grouped in `.form-group` pairs to keep the layout clean and symmetrical, especially on larger screens. On mobile, the form stacks vertically thanks to responsive grid rules.

---

## 🅱️ **Task B**

---

### **1. Website structure diagram – [5 Marks]**

Here's a detailed breakdown of the website structure and how navigation flows between different sections:

```
Homepage: index.html
│
├── .topbar → Location, Opening Hours, Contact Phone
├── .header → Logo + Navigation Menu (.navbar-list)
│
├── #home → Hero Image Slider
├── #about → Our Story + Team Members (.team-grid)
├── #menu → Event Menus (.menu-category & .menu-grid)
│   ├── Wedding
│   ├── Corporate
│   ├── Birthday
│   └── Special
│
├── #gallery → Event Gallery Grid (.gallery-grid)
├── #reviews → Client Testimonials with Slider
├── #contact → Contact Form + Company Info (.contact-form)
└── .footer → Quick Links, Services, Social Media, Address
```

Each of these sections is directly accessible from the navigation bar using anchor links like `#about`, `#menu`, etc., which provide a smooth scrolling experience thanks to JavaScript.

---

### **2. Testing on different browsers – [5 Marks]**

To ensure cross-browser compatibility, I tested the website on both **Google Chrome** and **Mozilla Firefox**. I focused on checking layout alignment, responsiveness, form behavior, slider transitions, and button functionalities.

Here’s what I noticed:

- The design appeared almost identical in both browsers.
- All sliders (hero and review) worked perfectly.
- Navigation toggle, form submission, and scroll-to-top button functioned the same.
- Font rendering was slightly different; Chrome rendered the text slightly sharper than Firefox.
- Default input field styles varied slightly—Firefox had a more pronounced border style.

But these were very minor differences. Functionally, everything behaved exactly as expected across both browsers.

---

### **3. Validating HTML with W3C Validator – [5 Marks]**

I ran my HTML file through the **W3C Validator** at [https://validator.w3.org](https://validator.w3.org) to check for any syntax or structural errors.

**Before validation:**
- The `<form>` tag didn’t have an `action` attribute. This triggered a warning.

**Fix:**
I added `action="#"` to make the form submit to the same page for now. Since there’s no backend, this placeholder still allows it to validate properly.

After fixing that, the rest of the HTML passed validation. I used proper nesting of elements, followed semantic structure, and made sure all tags were properly closed. There were no warnings or accessibility issues after that.

---

## 🅲️ **Part B – CSS (10 Marks)**

All styling for the website is written in a separate CSS file called `styles.css`, and it's linked in the `<head>` section of the HTML file.

### Key elements of my CSS implementation:

- **Custom variables** like `--primary`, `--secondary`, `--white`, etc., are declared at the top using `:root`. These help maintain a consistent color theme across the whole site.
- I used **Flexbox** for aligning navigation menus, team member cards, and contact info side-by-side.
- For layout sections like menus and the gallery, I used **CSS Grid**. The `.menu-grid` class ensures items are responsive and align neatly in multiple columns.
- I applied **transitions and hover effects** to elements like `.btn`, `.gallery-item`, and `.menu-item` to create smooth, interactive animations.
- **Media queries** were used at different breakpoints (992px, 768px, 576px) to adjust layout, font size, button spacing, and form structure. For example, `.form-group` stacks vertically on mobile.

This styling approach gave the site a polished, responsive, and modern look while ensuring maintainability and consistency.

---

## 🅳️ **Part C – JavaScript (10 Marks)**

I created an external JavaScript file called `script.js`, which adds dynamic behavior to the website and is linked at the bottom of the HTML file.

### Behaviors I implemented:

- **Hero Slider:** The `.hero-slider` changes slides every 5 seconds using a setInterval loop. Users can manually change slides using the `.prev` and `.next` buttons.
- **Scroll to Top Button:** The `.back-to-top` button appears when the user scrolls down the page and disappears when near the top. Clicking it scrolls the page smoothly to the top.
- **Mobile Navigation Toggle:** The `.nav-toggle` hamburger menu appears on smaller screens. Clicking it toggles the `.navbar-list` menu in and out.
- **Menu Category Switch:** I used event listeners on `.menu-category` buttons to switch between different menus (wedding, birthday, etc.) without reloading the page.
- **Form Validation:** Before submission, the script checks that all required fields (like name, email, phone, date) are filled in. If any field is missing, an alert message appears.

These interactive elements made the website feel dynamic and improved overall usability.

---

## 🅴️ **Part D – Critical Evaluation (10 Marks)**

**Final Evaluation (≈ 150 words):**

Working on the Sultan’s Dine website helped me understand how to build a complete frontend project from scratch. I used HTML to structure the site clearly, CSS to design an elegant and responsive layout, and JavaScript to make it interactive and functional.

The website works well on both mobile and desktop devices. The hero slider, menu tabs, testimonials section, and scroll-to-top button make the site engaging. I ensured accessibility and responsiveness were priorities throughout development.

If I were to improve the site in the future, I would add a backend system (like Firebase or PHP) to process the form data. I’d also add scroll-based animations to make the sections more visually dynamic. Connecting it to a CMS would allow easier content updates.

Overall, I’m proud of the work I did. It reflects real-world skills and shows I can build a professional, fully functional website.

---
