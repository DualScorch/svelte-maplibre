<script>
import '@skeletonlabs/skeleton/themes/theme-skeleton.css';

// This contains the bulk of Skeletons required styles:
import '@skeletonlabs/skeleton/styles/skeleton.css';

// Finally, your application's global stylesheet (sometimes labeled 'app.css')
import '../app.postcss';

  import { AppShell, AppBar, Drawer, drawerStore } from '@skeletonlabs/skeleton';

  import hljs from 'highlight.js';
  import 'highlight.js/styles/github-dark.css';
  import { storeHighlightJs } from '@skeletonlabs/skeleton';

  import NavBar from './NavBar.svelte';
  import LogoAndMenu from './LogoAndMenu.svelte';
</script>

<main class="w-full h-full">
  <slot />
</main>
