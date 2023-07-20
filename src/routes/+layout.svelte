<script>
import '@skeletonlabs/skeleton/themes/theme-skeleton.css';
import '@skeletonlabs/skeleton/styles/skeleton.css';
import '../app.postcss';

  import { AppShell, AppBar, Drawer, drawerStore } from '@skeletonlabs/skeleton';

  import 'highlight.js/styles/github-dark.css';

  import { computePosition, autoUpdate, offset, shift, flip, arrow } from '@floating-ui/dom';
  import { storePopup } from '@skeletonlabs/skeleton';
storePopup.set({ computePosition, autoUpdate, offset, shift, flip, arrow });
</script>
<AppShell
  slotHeader="h-16 variant-glass-surface !bg-black !bg-opacity-60 z-30 flex items-center justify-between px-4"
>
	<svelte:fragment slot="header">
    <span class="text-3xl font-medium ">Food <span class="text-xl">in</span> <span class="bg-gradient-to-r from-yellow-500 to-blue-700 bg-clip-text text-transparent box-decoration-clone" >Stockholm</span></span>
  </svelte:fragment>
	<!-- (sidebarLeft) -->
	<!-- (sidebarRight) -->
	<!-- (pageHeader) -->
	<!-- Router Slot -->
  <main class="w-full h-full">
    <slot />
  </main>
	<!-- ---- / ---- -->
	<!-- (pageFooter) -->
	<!-- (footer) -->
</AppShell>
