# NITDGP Website Frontend

> Frontend for the official website for NIT Durgapur

## Build Setup

```bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report
```
## Reusing components
### `CardTestimonial`
This shows small cards for representing people, communities, names,
etc. It has `name`, `image`, `desig` and `id` props. The `id` property
is meant to be used for faculty names having a faculty id.

This component is meant to be used under a `div` having `row` `class`
in it. Though it isn't mandatory. Its style can be controlled by
adding a custom class on the component.

#### Basic usage
```html
<template>
  <card-testimonial
    class="card-test" <!-- optionally override styles -->
    name="Hello World"
    image="https://imgs.xkcd.com/comics/python.png"
    desig="Programming Language"
  />
</template>
<script>
import CardTestimonial from '@/components/CardTestimonial'

export default {
  name: "compoNent"
  components: {
    CardTestimonial
  }
}
</script>
<style>
  .card-test {
    min-width: 230px !important;
    min-height: 300px !important;
    max-width: 500px !important;
    max-height: 500px !important;
    padding: 10px !important;
  }
</style>
```
